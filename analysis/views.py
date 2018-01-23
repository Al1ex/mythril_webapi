from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from analysis.models import Analysis
from analysis.serializers import *
import uuid as uu


@api_view(['GET', 'POST'])
def bytecode_submission(request):
	"""
	Submits a new analysis with a smart contract bytecode
	"""
	if request.method == 'GET':
		all_analysis = Analysis.objects.all()
		serializer = AnalysisSerializer(all_analysis, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = AnalysisSerializer(data=request.data)
		if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def status(request, uuid):
	"""
	Returns the status of an analysis for a given UUID.
	"""
	analysis = Analysis.objects.filter(uuid=uuid).first()
	serializer = AnalysisStatusSerializer(analysis)
	return Response(serializer.data)



@api_view(['GET'])
def report(request, uuid):
	"""
	Returns the report of the issues found in an analysis for a given UUID.
	"""
	analysis = Analysis.objects.filter(uuid=uuid).first()
	serializer = AnalysisReportSerializer(analysis)
	return Response(serializer.data)


