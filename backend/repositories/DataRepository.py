from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    @staticmethod
    def read_status_lampen():
        sql = "SELECT * from lampen"
        return Database.get_rows(sql)

    @staticmethod
    def read_status_lamp_by_id(id):
        sql = "SELECT * from lampen WHERE id = %s"
        params = [id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def update_status_lamp(id, status):
        sql = "UPDATE lampen SET status = %s WHERE id = %s"
        params = [status, id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_status_alle_lampen(status):
        sql = "UPDATE lampen SET status = %s"
        params = [status]
        return Database.execute_sql(sql, params)


    @staticmethod
    def insert_data(deviceid,actieid , actiedatum , waarde, commentaar ):
        sql = "INSERT INTO Historiek (deviceid , actieid , actiedatum , waarde , commentaar ) VALUES  (%s, %s, %s, %s, %s)" 
        params= [deviceid,actieid ,actiedatum , waarde, commentaar]
        return Database.execute_sql(sql, params)
    
    
    @staticmethod
    def historiek_data_ophalen():
        sql = "SELECT volgnummer , deviceid, actiedatum , waarde , commentaar from Historiek Order by volgnummer Desc limit 50"
        return Database.get_rows(sql)
    
    @staticmethod
    def ophalen_vragen():
        sql = "SELECT * from vraag order by RAND() limit 6"
        return Database.get_rows(sql)
    
    @staticmethod
    def add_speler(naam,kaartnummer,datum_gespeeld,time_played):
        sql = "INSERT INTO speler (naam , kaartnummer, datum_gespeeld, time_played ) VALUES (%s,%s,%s,%s)"
        params = [naam, kaartnummer, datum_gespeeld, time_played]
        return Database.execute_sql(sql, params)
    
    # @staticmethod
    # def update_speler(spelerid,time_played):
    #     sql = "UPDATE speler SET time_played = %s WHERE spelerid = %s"
    #     params = [time_played, spelerid]
    #     return Database.execute_sql(sql, params)
    
    @staticmethod
    def update_tijden(spel_1,spel_2,spel_3,spel_4,totale_tijd,spelerid):
        sql = "insert into tijd (spel_1,spel_2,spel_3,spel_4,totale_tijd,spelerid) values (%s,%s,%s,%s,%s,%s)"
        params = [spel_1,spel_2,spel_3,spel_4,totale_tijd,spelerid]
        return Database.execute_sql(sql, params)    
    
    @staticmethod
    def get_tijden(spelerid):
        sql = "SELECT * FROM tijd WHERE spelerid = %s"
        params = [spelerid]
        return Database.get_one_row(sql,params)
    
    
    @staticmethod 
    def get_top_times():
        sql = "select * from tijd order by totale_tijd limit 3"
        return Database.get_rows(sql)
    
    @staticmethod
    def add_speler(naam,kaartnummer,datum_gespeeld):
        sql = "INSERT INTO speler (naam , kaartnummer, datum_gespeeld) VALUES (%s,%s,%s)"
        params = [naam, kaartnummer, datum_gespeeld]
        return Database.execute_sql(sql, params)