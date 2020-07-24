import json

from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from meilleur_corpo.apps.estate_adverts.forms import EstateAdvertsSearchForm

class EstateAdvertsView(APIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        search_form = EstateAdvertsSearchForm(json.loads(request.body))

        if search_form.is_valid():
            result = self.get_result(
                """
                    SELECT
                        AVG(condominium_expenses) as condominium_expenses_avg
                    FROM estate_adverts
                        WHERE 1
                """,
                search_form.cleaned_data,
            )

            result.update(
                self.get_result(
                    """
                        SELECT
                            AVG(condominium_expenses) as condominium_expenses_avg_1O
                        FROM estate_adverts
                            WHERE condominium_expenses >= 0.1 * (SELECT MAX(condominium_expenses) FROM estate_adverts)
                    """,
                    search_form.cleaned_data,
                )
            )

            result.update(
                self.get_result(
                    """
                        SELECT
                            AVG(condominium_expenses) as condominium_expenses_avg_9O
                        FROM estate_adverts
                            WHERE condominium_expenses <= 0.9 * (SELECT MAX(condominium_expenses) FROM estate_adverts)
                    """,
                    search_form.cleaned_data,
                )
            )

            return Response(result)
        else:
            return Response(dict(form.errors.items()))

    def get_result(self, query, data={}):
        cursor = connection.cursor()

        for key, value in data.items():
            if value != '':
                if isinstance(value, bool):
                    value = int(value)
                query += " AND %s = '%s'" % (key, value)

        cursor.execute(query)
        return dict(zip([col[0] for col in cursor.description], [str(row) for row in cursor.fetchone()]))
