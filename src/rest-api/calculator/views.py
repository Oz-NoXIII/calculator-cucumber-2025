from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalculationSerializer

import sys
import os

# Add the parent directory of src to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(project_root)

# Now we can import using the absolute path starting with src
from src.main.python.parsing.expression_parser import parse_expression
from src.main.python.calculator.calculator import eval_expression



class CalculatorAPIView(APIView):
    def post(self, request):
        serializer = CalculationSerializer(data=request.data)
        if serializer.is_valid():
            expression = serializer.validated_data['expression']
            try:
                # Parse and evaluate the expression
                parsed_expr = parse_expression(expression)
                result = eval_expression(parsed_expr)
                
                # Handle different result types
                if hasattr(result, 'get_value'):
                    result_value = result.get_value()
                else:
                    result_value = result
                
                return Response({'result': str(result_value)}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)