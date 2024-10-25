class GestionCobroHandler:
    def __init__(self, request):
        self.request = request

    def guardar_datos_cobro(self):
        
        dinero_actual = self.request.POST.get("dinero-actual", "")
        sentido_cobro = self.request.POST.get("sentido-cobro", "")

        
        self.request.session["dinero_actual"] = dinero_actual
        self.request.session["sentido_cobro"] = sentido_cobro

    def obtener_datos_cobro(self):
        
        dinero_actual = self.request.session.get("dinero_actual", "0")
        sentido_cobro = self.request.session.get("sentido_cobro", "Entrada")
        return dinero_actual, sentido_cobro

    
