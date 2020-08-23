class personinfo:
    
    def __init__(self,accountid,fname,sname,sex,birthday,idCard,phoneNumber,email,nation,race):
       self.accountid =accountid
       self.fname = fname
       self.sname = sname
       self.birthday = birthday
       self.sex = sex
       self.idCard = idCard
       self.phoneNumber = phoneNumber
       self.email = email
       self.nation = nation
       self.race = race
    def sexinfo(self):
        if (self.sex==1):
            return "ชาย"
        elif(self.sex==2) :
            return"หญิง"
        else:
            return "ไม่ระบุุ"
class personHistory:
    def __init__(self,accountid,historyCa,breastCheck,bCAyear,bothbeastCheck,bovalCheck,bovalyear,bgutCheck,bgutyear,liverCheck,liveryear,postGrandCheck,postGrandyear,skinCheck,skinyear):
        self.accountid = accountid
        self.historyCa = historyCa
        self.breastCheck = breastCheck
        self.bCAyear = bCAyear
        self.bothbeastCheck = bothbeastCheck
        self.bovalCheck =bovalCheck
        self.bovalyear = bovalyear
        self.bgutCheck = bgutCheck
        self.bgutyear = bgutyear
        self.liverCheck = liverCheck
        self.liveryear = liveryear
        self.postGrandCheck = postGrandCheck
        self.postGrandyear = postGrandyear
        self.skinCheck = skinCheck
        self.skinyear = skinyear

