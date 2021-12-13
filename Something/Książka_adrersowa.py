class BaseContact:
     def __init__(self, first_name, last_name, tel, email):
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.email = email
        self._label_length = len(self.first_name) + len(self.last_name)
    
number_1 = BaseContact(first_name="Marlin", last_name="Hayes", tel="76-805-04-46", position="Central Brand Manager", email="Maudie.Jacobson44@yahoo.com")
number_2 = BaseContact(first_name="Carmel", last_name="Wilkinson", tel="42-467-19-88", position="Human Solutions Agent", email="Erwin95@yahoo.com")
number_3 = BaseContact(first_name="Jerel", last_name="Collins", tel="46-800-20-67", position="Dynamic Directives Producer", email="Diego41@hotmail.com")
number_4 = BaseContact(first_name="Laron", last_name="Kris", tel="33-395-14-20", position="District Response Facilitator", email="Buddy87@gmail.com")
number_5 = BaseContact(first_name="Izaiah", last_name="Adams", tel="86-379-63-32", position="Forward Web Representative", email="Tevin_Brakus@yahoo.com")

print(number_1.first_name)


class BusinessContact(BaseContact):
    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone

number_1 = BusinessContact(company="Keebler", position="Central Brand Manager", business_phone="41-265-45-05")
number_2 = BusinessContact(company="Harvey LLC", position="Human Solutions Agent", business_phonel="67-517-06-62")
number_3 = BusinessContact(company="Christiansen, Altenwerth and Fahey", position="Dynamic Directives Producer", business_phone="68-010-99-75")
number_4 = BusinessContact(company="Herzog - Rau", position="District Response Facilitator", business_phone="86-049-26-13")
number_5 = BusinessContact(company="Jerde LLC", position="Forward Web Representative", business_phone="52-974-95-59")

