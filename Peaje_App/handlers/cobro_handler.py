from django.shortcuts import render

class CobroHandler:
    @staticmethod
    def handle_get(request):
        return render(request, 'cobro.html')

    @staticmethod
    def handle_post(request):
        sentido_cobro = request.POST.get('sentido-cobro')
        numero_casilla = request.POST.get('numero-casilla')
        return render(request, 'cobro.html', {
            'sentido_cobro': sentido_cobro,
            'numero_casilla': numero_casilla
        })
