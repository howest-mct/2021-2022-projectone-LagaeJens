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
    def insert_data(deviceid,actieid ,spelerid, actiedatum , waarde, commentaar ):
        sql = "INSERT INTO Historiek (deviceid , actieid , spelerid, actiedatum , waarde , commentaar ) VALUES  (%s, %s, %s, %s, %s, %s)" 
        params= [deviceid,actieid ,spelerid, actiedatum , waarde, commentaar]
        return Database.execute_sql(sql, params)
    
    
    @staticmethod
    def historiek_data_ophalen():
        sql = "SELECT * from Historiek Order by volgnummer Desc"
        return Database.get_rows(sql)