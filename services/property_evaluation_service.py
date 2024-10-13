from spyne import Application, rpc, ServiceBase, Unicode, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class PropertyEvaluationService(ServiceBase):
    
    @rpc(Unicode, Unicode, _returns=Float)
    def evaluate_property(ctx, property_description, address):
        # Simulate property value evaluation (based on description and address)
        property_value = 250000  # You can adjust this logic as needed
        return property_value

# Créer l'application Spyne
application = Application([PropertyEvaluationService],
                          tns='property_evaluation_service',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    wsgi_application = WsgiApplication(application)
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8003, wsgi_application)
    print("Property Evaluation Service started on http://localhost:8003")
    server.serve_forever()
