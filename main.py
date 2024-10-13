import subprocess
import time

# Liste des services à lancer
services = [
    {"name": "Information Extraction Service", "script": "services/information_extraction_service.py"},
    {"name": "Solvency Check Service", "script": "services/solvency_check_service.py"},
    {"name": "Property Evaluation Service", "script": "services/property_evaluation_service.py"},
    {"name": "Approval Decision Service", "script": "services/approval_decision_service.py"},
    {"name": "Composite Loan Evaluation Service", "script": "web_composite_service.py"},
    {"name": "Watchdog Trigger", "script": "watchdog_trigger.py"}
]

processes = []

def launch_service(service):
    try:
        # Lancer le service en arrière-plan
        process = subprocess.Popen(["python", service["script"]])
        processes.append(process)
        print(f"{service['name']} lancé avec succès.")
    except Exception as e:
        print(f"Erreur lors du lancement de {service['name']}: {str(e)}")

if __name__ == "__main__":
    print("Lancement de tous les services...")

    # Lancer chaque service
    for service in services:
        launch_service(service)
        time.sleep(1)  # Délai pour permettre à chaque service de démarrer correctement

    print("Tous les services sont en cours d'exécution.")

    # Attendre l'arrêt manuel (Ctrl+C)
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print("Arrêt des services...")
        for process in processes:
            process.terminate()
        print("Tous les services sont arrêtés.")
