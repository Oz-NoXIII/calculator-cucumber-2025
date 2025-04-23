from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalculationSerializer

class CalculatorAPIView(APIView):
    def post(self, request):
        serializer = CalculationSerializer(data=request.data)
        if serializer.is_valid():
            expression = serializer.validated_data['expression']
            try:
                # TODO: evaluate
                print(expression)
                result = expression
                return Response({'result': result}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)