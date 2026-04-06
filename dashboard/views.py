from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from records.models import Record
from django.db.models import Sum

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Base queryset (role-based access)
        if user.role == 'admin':
            queryset = Record.objects.all()
        else:
            queryset = Record.objects.filter(created_by=user)

        # Total Income
        total_income = queryset.filter(type='income').aggregate(
            total=Sum('amount')
        )['total'] or 0

        # Total Expense
        total_expense = queryset.filter(type='expense').aggregate(
            total=Sum('amount')
        )['total'] or 0

        # Net Balance
        net_balance = total_income - total_expense

        # Recent Transactions (last 5)
        recent_transactions = queryset.order_by('-date')[:5].values(
            'id', 'category', 'amount', 'type', 'date'
        )

        # Category-wise summary (separate income/expense)
        category_summary = queryset.values('category', 'type').annotate(
            total=Sum('amount')
        )

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": net_balance,
            "total_records": queryset.count(),
            "recent_transactions": list(recent_transactions),
            "category_summary": list(category_summary)
        })