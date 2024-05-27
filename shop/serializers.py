from rest_framework import serializers

from shop.models import Plan, Transaction


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'


class AddTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = []

    def save(self, **kwargs):
        transaction = Transaction(user=self.context['user'],
                                  price=self.context['price'],
                                  gateway=self.context['gateway'],
                                  gateway_code=self.context['gateway_code'],
                                  plan_id=self.context['plan'],
                                  package_name=self.context['package_name'],
                                  description=self.context['description'])
        transaction.save()
        return transaction
