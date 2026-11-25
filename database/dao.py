from database.DB_connect import DBConnect
from model.filiale import Filiale

class DAO:

    @staticmethod
    def get_nodi():
        cnx = DBConnect.get_connection()
        nodi =[]

        if cnx is None :
            print("errore di connessione al DB")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT id, codice, nome, citta, provincia, latitudine, longitudine FROM filiale"
        try:
            cursor.execute(query)
            for line in cursor:
                f = Filiale(int(line["id"]),
                            line["codice"], line["nome"], line["citta"],line["provincia"],
                            float(line["latitudine"]), float(line["longitudine"]))
                nodi.append(f)

        except Exception as e:
            print(f"Errore durante la query get_nodi: {e}")
            nodi = None
        finally:
            cursor.close()
            cnx.close()

        return nodi


    @staticmethod
    def get_archi():
        cnx = DBConnect.get_connection()

        archi = []
        if cnx is None :
            print("errore di connessione al DB")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT LEAST(id_filiale_origine, id_filiale_destinazione) AS f1,
                        GREATEST(id_filiale_origine, id_filiale_destinazione) AS f2,
                        AVG(importo) AS peso,
                        FROM bonifico
                        GROUP BY f1, f2"""

        try:
            cursor.execute(query)
            for a in cursor:
                archi.append([int(a["f1"]),int(a["f2"]),float(a["peso"])])


        except Exception as e:
            print(f"Errore durante la query get_archi: {e}")
            archi = None
        finally:
            cursor.close()
            cnx.close()

        return archi