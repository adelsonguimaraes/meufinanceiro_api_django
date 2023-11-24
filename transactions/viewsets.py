from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from transactions import models, serializers, actions, filters


class CreditCardModelViewSet(viewsets.ModelViewSet):
    queryset = models.CreditCard.objects.all()
    serializer_class = serializers.CreditCardSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super(CreditCardModelViewSet, self).create(request, *args, **kwargs)

    @action(methods=['GET'], detail=False)
    def flags(self, request):
        response = actions.CreditCard.get_choices()
        return Response(data=response, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def current_transactions(self, request):
        response = actions.CreditCard.get_current_transactions(
            month=request.query_params.get('month'), year=request.query_params.get('year')
        )
        return Response(data=response, status=status.HTTP_200_OK)


class TransactionModelViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

    def create(self, request, *args, **kwargs):
        if not request.data['user']:
            request.data['user'] = request.user.id

        response = super(TransactionModelViewSet, self).create(request, *args, **kwargs)
        actions.TransactionAction.generate_portion_transaction(transaction=response.data.serializer.instance)
        return Response(status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        response = super(TransactionModelViewSet, self).update(request, *args, **kwargs)
        actions.TransactionAction.update_portions_transaction(transaction=response.data.serializer.instance)
        return Response(response.data, status=status.HTTP_200_OK)


class TransactionPortionModelViewSet(viewsets.ModelViewSet):
    queryset = models.TransactionPortion.objects.all()
    serializer_class = serializers.TransactionPortionSerializer
    filterset_class = filters.TransactionPortionFilter
    ordering_fields = ['due_date']
    ordering = ['due_date']

    @action(methods=['get'], detail=False)
    def get_months(self, request, *args, **kwargs):
        response = actions.TransactionPortionAction.generate_months_transitions()
        return Response({'data': response}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def teste(self, request, *args, **kwargs):
        # date = datetime.strptime(__date_string='2023-07-09', __format='%Y-%m-%d')
        # models.TransactionPortion.objects.filter(created_at__year=date.year, created_at__month=date.month,
        #                                          created_at__day=date.day)

        a = super().list(request, *args, **kwargs)

        res = actions.TransactionPortionAction.teste(queryset=self.queryset)
        return Response(res, status.HTTP_200_OK)