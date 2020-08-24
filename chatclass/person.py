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
#ประวัติส่วนตัว
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
# ประวัติลูกชาย
class sonHistory:
    def __init__(self,accountid,optionhistoryson,sonbreastcheck,sonbreatyear,sonliverCheck,sonliveryear,songutCheck,songutyear,sonpostGrandCheck,sonpostGrandrYear,sonskinCheck,sonskinyear):
       self.accountid = accountid
       self.optionhistoryson= optionhistoryson
       self.sonbreastcheck = sonbreastcheck
       self.sonbreatyear =sonbreatyear
       self.sonliverCheck =sonliverCheck
       self.sonliveryear =sonliveryear
       self.songutCheck =songutCheck
       self.songutyear = songutyear
       self.sonpostGrandCheck = sonpostGrandCheck
       self.sonpostGrandrYear = sonpostGrandrYear
       self.sonskinCheck = sonskinCheck
       self.sonskinyear =sonskinyear
#ประวัติลูกสาว
class daughterHistory:
    def __init__(self,acoountid,optionhistorydaughter,daughterbreastCheck,daughterbreastyear,daughterliverCheck,daughterliveryear,daughtergutcheck,daughtergutyear,daughterpostGrandCheck,daughterpostGrandyear,daughterskinChek,daughterskinyear):
        self.accountid = acoountid
        self.optionhistorydaughter = optionhistorydaughter
        self.daughterbreastCheck =  daughterbreastCheck
        self.daughterbreastyear = daughterbreastyear
        self.daughterliverCheck = daughterliverCheck
        self.daughterliveryear =daughterliveryear
        self.daughtergutcheck = daughtergutcheck
        self.daughtergutyear = daughtergutyear
        self.daughterpostGrandCheck =daughterpostGrandCheck
        self.daughterpostGrandCheck = daughterpostGrandyear
        self.daughterskinChek = daughterskinChek
        self.daughterskinyear =daughterskinyear
#ประวัติพ่อ
class fatherHistory:
    def __init__(self,accountid,optionhistoryfather,fatherbreatCheck,fatherbreastyear,fatherliverCheck,fatherliveryear,fathergutCheck,fathergutyear,fatherpostGrandCheck,fartherpostGrandyear,fatherskinCheck,fatherskinyear):
        self.accountid =  accountid
        self.optionhistoryfather =optionhistoryfather
        self.fatherbreatCheck =fatherbreatCheck
        self.fatherbreastyear = fatherbreastyear
        self.fatherliverCheck =fatherliverCheck
        self.fatherliveryear = fatherliveryear
        self.fathergutCheck = fathergutCheck
        self.fathergutyear = fathergutyear
        self.fatherpostGrandCheck = fatherpostGrandCheck
        self.fartherpostGrandyear = fartherpostGrandyear
        self.fatherskinCheck = fatherskinCheck
        self.fatherskinyear = fatherskinyear
#ประวัติแม่
class motherHistory:
    def __init__(self,accountid,optionhistorymother,motherbreastCheck,motherbreatyear,motherliverCheck,motherliveryear,mothergutCheck,mothergutyear,motherpostGrandCheck,motherpostGrandyear,motherskinCheck,motherskinyear):
       self.accountid = accountid
       self.optionhistorymother = optionhistorymother
       self.motherbreastCheck = motherbreastCheck
       self.motherbreastyear = motherbreatyear
       self.motherliverCheck =motherliverCheck
       self.motherliveryear = motherliveryear
       self.mothergutCheck = mothergutCheck
       self.mothergutyear = mothergutyear
       self.motherpostGrandCheck = motherpostGrandCheck
       self.motherpostGrandyear = motherpostGrandyear
       self.motherskinCheck = motherskinCheck
       self.motherskinyear = motherskinyear
#ประวัติน้องชาย
class brotherHistory:
    def __init__(self,accountid,optionhistorylbrother,brotherbreastCheck,brotherbreastyear,brotherliverCheck,brotherliveryear,brothergutCheck,brothergutyear,broherpostGrandCheck,brotherpostGrandyear,brotherskinCheck,brotherskinyear):
       self.accountid = accountid
       self.optionhistorylbrother = optionhistorylbrother
       self.brotherbreastCheck = brotherbreastCheck
       self.brotherbreastyear = brotherbreastyear
       self.brotherlivercheck = brotherliverCheck
       self.brotherliveryear =  brotherliveryear
       self.brothergutCheck = brothergutCheck
       self.brothergutyear = brothergutyear
       self.brotherpostGrandCheck = broherpostGrandCheck
       self.brotherpostGrandyear =brotherpostGrandyear
       self.brotherskinCheck = brotherskinCheck
       self.brotherskinyear = brotherskinyear
#ประวัติน้องหญิง
class sisterHistory:
    def __init__(self,accountid,optionhistorylsister,sisterbreastCheck,sisterbreastyear,sisterliverCheck,sisterliveryear,sistergutCheck,sistergutyear,sisterpostGrandCheck,sisterpostGrandyear,sisterskinCheck,sisterskinyear):
       self.accountid = accountid
       self.optionhistorylsister =optionhistorylsister
       self.sisterbreastCheck = sisterbreastCheck
       self.sisterbreastyear =sisterbreastyear
       self.sisterliverCheck = sisterliverCheck 
       self.sisterliveryear = sisterliveryear
       self.sistergutCheck = sistergutCheck
       self.sistergutyear =sistergutyear
       self.sisterpostGrandCheck = sisterpostGrandCheck
       self.sisterpostGrandyear = sisterpostGrandyear
       self.sisterskinCheck = sisterskinCheck
       self.sisterskinyear =sisterskinyear
#ประวัติทวดชาย
class mangrandFaHistory:
    def __init__(self,accountid,optionhistorymangrandfather,mangrandFabreastCheck,mangrandFabreastyear,mangrandFaliverCheck,mangrandFaliveryear,mangrandFagutCheck,mangrandFagutyear,mangrandFapostGrandCheck,mangrandFapostGrandyear,mangrandFaskinCheck,mangrandFaskinyear):
       self.accountid = accountid
       self.optionhistorymangrandfather = optionhistorymangrandfather
       self.mangrandFabreastCheck =mangrandFabreastCheck
       self.mangrandFabreastyear =mangrandFabreastyear
       self.mangrandFaliverCheck =mangrandFaliverCheck
       self.mangrandFaliveryear =mangrandFaliveryear
       self.mangrandFagutCheck = mangrandFagutCheck
       self.mangrandFagutyear =mangrandFagutyear
       self.mangrandFapostGrandCheck =mangrandFapostGrandCheck
       self.mangrandFapostGrandyear = mangrandFapostGrandyear
       self.mangrandFaskinCheck =mangrandFaskinCheck
       self.mangrandFaskinyear =mangrandFaskinyear
#ประวัติทวดหญิง

