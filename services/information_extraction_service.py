import re
from spyne import Application, rpc, ServiceBase, ComplexModel, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Define a complex type for key-value pairs
class DictionaryItem(ComplexModel):
    key = Unicode
    value = Unicode

class InformationExtractionService(ServiceBase):
    @rpc(Unicode, _returns=DictionaryItem)
    def extract_loan_information(ctx, loan_request):
        # Extract data using regex
        try:
            nom = re.search(r'Nom du Client: (.+)', loan_request).group(1)
            adresse = re.search(r'Adresse: (.+)', loan_request).group(1)
            email = re.search(r'Email: (.+)', loan_request).group(1)
            telephone = re.search(r'Numéro de Téléphone: (.+)', loan_request).group(1)
            montant = int(re.search(r'Montant du Prêt Demandé: (\d+) EUR', loan_request).group(1))
            duree = int(re.search(r'Durée du Prêt: (\d+) ans', loan_request).group(1))
            description_propriete = re.search(r'Description de la Propriété: (.+)', loan_request).group(1)
            revenu_mensuel = int(re.search(r'Revenu Mensuel: (\d+) EUR', loan_request).group(1))
            depenses_mensuelles = int(re.search(r'Dépenses Mensuelles: (\d+) EUR', loan_request).group(1))

            # Create dictionary
            extracted_info = {
                "Nom": nom,
                "Adresse": adresse,
                "Email": email,
                "Téléphone": telephone,
                "Montant du Prêt": montant,
                "Durée": duree,
                "Description de la Propriété": description_propriete,
                "Revenu Mensuel": revenu_mensuel,
                "Dépenses Mensuelles": depenses_mensuelles
            }
            return DictionaryItem(key="extracted_info", value=str(extracted_info))
        except Exception as e:
            return DictionaryItem(key="error", value="Extraction failed: " + str(e))

# Create a Spyne application
application = Application([InformationExtractionService],
                          tns='information.extraction.service',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    wsgi_application = WsgiApplication(application)
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8001, wsgi_application)
    print("Information Extraction Service started on http://localhost:8001")
    server.serve_forever()
