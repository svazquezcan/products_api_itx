from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
import requests
from concurrent.futures import ThreadPoolExecutor
from django.core.cache import cache


class SimilarProductsView(APIView):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('productId')

        base_url = "http://host.docker.internal:3001/product"

        similar_products_url = f"{base_url}/{product_id}/similarids"
        similar_products_response = requests.get(similar_products_url)

        if similar_products_response.status_code != 200:
            raise NotFound(detail="Similar products not found.")

        try:
            similar_products = similar_products_response.json()
        except ValueError:
            return Response({"detail": "Invalid response format for similar products."},
                            status=status.HTTP_400_BAD_REQUEST)

        response = []
        with ThreadPoolExecutor(max_workers=64) as executor:
            futures = []
            for similar_product_id in similar_products:
                similar_product_info_url = f"{base_url}/{similar_product_id}"
                futures.append(executor.submit(self.get_similar_product_info, similar_product_info_url))

            for future in futures:
                similar_product_info = future.result()
                if similar_product_info:
                    response.append(similar_product_info)

        return Response(response, status=status.HTTP_200_OK)

    def get_similar_product_info(self, url):
        """Helper method to fetch product information and cache it."""
        cached_similar_product_info = cache.get(url)
        if cached_similar_product_info:
            return cached_similar_product_info

        try:
            product_response = requests.get(url)
            if product_response.status_code == 200:
                similar_product_info = product_response.json()
                cache.set(url, similar_product_info, timeout=300)
                return similar_product_info
            return None
        except requests.RequestException:
            return None
