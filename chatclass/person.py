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
    def __init__(self,accountid,optionhistoryson,sonbreastcheck,sonbreastyear,sonliverCheck,sonliveryear,songutCheck,songutyear,sonpostGrandCheck,sonpostGrandYear,sonskinCheck,sonskinyear):
       self.accountid = accountid
       self.optionhistoryson= optionhistoryson
       self.sonbreastcheck = sonbreastcheck
       self.sonbreastyear =sonbreastyear
       self.sonliverCheck =sonliverCheck
       self.sonliveryear =sonliveryear
       self.songutCheck =songutCheck
       self.songutyear = songutyear
       self.sonpostGrandCheck = sonpostGrandCheck
       self.sonpostGrandYear = sonpostGrandYear
       self.sonskinCheck = sonskinCheck
       self.sonskinyear =sonskinyear
#ประวัติลูกสาว
class daughterHistory:
    def __init__(self,accountid,optionhistorydaughter,daughterbreastCheck,daughterbreastyear,daughterliverCheck,daughterliveryear,daughtergutCheck,daughtergutyear,daughterpostGrandCheck,daughterpostGrandyear,daughterskinCheck,daughterskinyear):
        self.accountid = accountid
        self.optionhistorydaughter = optionhistorydaughter
        self.daughterbreastCheck =  daughterbreastCheck
        self.daughterbreastyear = daughterbreastyear
        self.daughterliverCheck = daughterliverCheck
        self.daughterliveryear =daughterliveryear
        self.daughtergutCheck = daughtergutCheck
        self.daughtergutyear = daughtergutyear
        self.daughterpostGrandCheck =daughterpostGrandCheck
        self.daughterpostGrandyear = daughterpostGrandyear
        self.daughterskinCheck = daughterskinCheck
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
    def __init__(self,accountid,optionhistorymother,motherbreastCheck,motherbreastyear,motherliverCheck,motherliveryear,mothergutCheck,mothergutyear,motherpostGrandCheck,motherpostGrandyear,motherskinCheck,motherskinyear):
       self.accountid = accountid
       self.optionhistorymother = optionhistorymother
       self.motherbreastCheck = motherbreastCheck
       self.motherbreastyear = motherbreastyear
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
    def __init__(self,accountid,optionhistorysister,sisterbreastCheck,sisterbreastyear,sisterliverCheck,sisterliveryear,sistergutCheck,sistergutyear,sisterpostGrandCheck,sisterpostGrandyear,sisterskinCheck,sisterskinyear):
       self.accountid = accountid
       self.optionhistorysister =optionhistorysister
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
class womangranMomHistory:
    def __init__(self,accountid,optionhistorywomangrandmother,womangrandMomCheck,womangrandMomyear,womangrandliverCheck,womangrandliveryear,womangrandgutCheck,womangrandgutyear,womangrandpostGrandCheck,womangrandpostGrandyear,womangrandskinCheck,womangrandskinyear):
        self.accountid = accountid
        self.optionhistorywomangrandmother =optionhistorywomangrandmother
        self.womangrandMomCheck =womangrandMomCheck
        self.womangrandMomyear =womangrandMomyear
        self.womangrandMomliverCheck = womangrandliverCheck
        self.womangrandMomliveryear = womangrandliveryear
        self.womandgrandgutCheck = womangrandgutCheck
        self.womangrandgutyear = womangrandgutyear
        self.womangrandpostGrandCheck =womangrandpostGrandCheck
        self.womangrandpostGrandyear = womangrandpostGrandyear
        self.womangrandskinCheck = womangrandskinCheck
        self.womangrandskinyear = womangrandskinyear
#ประวัติปู่
class grandFatherHistory:
    def __init__(self,accountid,optionhistoryfgrandfather,grandFatherbreastCheck,grandFatherbreastyear,grandFatherliverCheck,grandFatherliveryear,grandFathergutCheck,grandFatherguyear,grandFatherpostGrandCheck,grandFatherpostGrandyear,grandFatherskinsCheck,grandFatherskinyear):
        self.accountid = accountid
        self.optionhistorygrandfather = optionhistoryfgrandfather
        self.grandFatherbreastCheck =grandFatherbreastCheck
        self.grandFatherbreastyear =grandFatherbreastyear
        self.grandFartherliverCheck =grandFatherliverCheck
        self.grandFatherliveryear = grandFatherliveryear
        self.grandFathergutCheck = grandFathergutCheck
        self.granFathergutyear = grandFatherguyear
        self.grandFatherpostgrandCheck =grandFatherpostGrandCheck
        self.grandFatherpostGrandyear =grandFatherpostGrandyear
        self.grandFatherskinsCheck =grandFatherskinsCheck
        self.grandFatherskinyear = grandFatherskinyear
#ประวัติย่า
class grandMomHistory:
    def __init__(self,accountid,optionhistorygrandmother,grandMombreastCheck,grandMombreastyear,grandMomliverCheck,grandMomliveryear,grandMomgutCheck,grandMomgutyear,grandMompostGrandCheck,grandMompostGrandyear,grandMomskinCheck,grandMomskinyear):
        self.accountid =accountid
        self.optionhistorygrandmother = optionhistorygrandmother
        self.grandMombreastCheck =grandMombreastCheck
        self.grandMombreastyear =grandMombreastyear
        self.grandMomliverCheck =grandMomliverCheck
        self.grandMomliveryear =grandMomliveryear
        self.grandMomgutCheck =grandMomgutCheck
        self.grandMomgutyear =grandMomgutyear
        self.grandMompostGrandCheck =grandMompostGrandCheck
        self.grandMompostGrandyear = grandMompostGrandyear
        self.grandMomskinCheck =grandMomskinCheck
        self.grandMomskinyear =grandMomskinyear
#ประวัติตา
class fatherOfMomHistory:
    def __init__(self,accountid,optionhistoryfathermom,fatherOfMombreastCheck,fatherOfMombreastyear,fatherOfMomliverCheck,fatherOfMomliveryear,fatherOfMomgutCheck,fatherOfMomgutyear,fatherOfMompostGrandCheck,fatherOfMompostGrandyear,fatherOfMomskinCheck,fatherOfMomskinyear):   
      self.accountid =accountid
      self.optionhistoryfathermom = optionhistoryfathermom
      self.fatherOfMombreastCheck = fatherOfMombreastCheck
      self.fatherOfMombreastyear =fatherOfMombreastyear
      self.fatherOfMomliverCheck =fatherOfMomliverCheck
      self.fatherOfMomliveryear = fatherOfMomliveryear
      self.fatherOfMomgutCheck =fatherOfMomgutCheck
      self.fatherOfMomgutyear =fatherOfMomgutyear
      self.fatherOfMompostGrandCheck =fatherOfMompostGrandCheck
      self.fatherOfMompostGrandyear =fatherOfMompostGrandyear
      self.fatherOfMomskinCheck =fatherOfMomskinCheck
      self.fatherOfMomskinyear =fatherOfMomskinyear
#ประวัติยาย
class motherOfMomHistory:
    def __init__(self,accountid,optionhistorymothermom,motherOfMombreastCheck,motherOfMombreastyear,motherOfMomliverCheck,motherOfMomliveryear,motherOfMomgutCheck,motherOfMomgutyear,motherOfMompostGrandCheck,motherOfMompostGrandyear,motherOfMomskinCheck,motherOfMomskinyear):
       self.accountid = accountid
       self.optonhistorymothermom =optionhistorymothermom
       self.motherOfMombreastCheck =motherOfMombreastCheck
       self.motherOfMombreastyear =motherOfMombreastyear
       self.motherOfMomliverCheck =motherOfMomliverCheck
       self.motherOfMomliveryear =motherOfMomliveryear
       self.motherOfMomgutCheck = motherOfMomgutCheck
       self.motherOfMomgutyear =motherOfMomgutyear
       self.motherOfMompostGrandCheck = motherOfMompostGrandCheck
       self.motherOfMompostGrandyear =motherOfMompostGrandyear
       self.motherOfMomskinCheck = motherOfMomskinCheck
       self.motherOfMomskinyear =motherOfMomskinyear
#ประวัติลุง
class bigUncleHistory:
    def __init__(self,accountid,optionhistorybiguncle,bigunclebreastCheck,bigunclebreastyear,biguncleliverCheck,biguncleliveryear,bigunclegutCheck,bigunclegutyear,bigunclepostGrandCheck,bigunclepostGrandyear,biguncleskinCheck,biguncleskinyear):
        self.accountid = accountid
        self.optionhistorybiguncle =optionhistorybiguncle
        self.bigunclebreastCheck = bigunclebreastCheck
        self.bigunclebreastyear =bigunclebreastyear
        self.biguncleliverCheck = biguncleliverCheck
        self.biguncleliveryear =biguncleliveryear
        self.bigunclegutCheck =bigunclegutCheck
        self.bigunclegutyear =bigunclegutyear
        self.bigunclepostGrandCheck = bigunclepostGrandCheck
        self.bigunclepsotGrandyear =  bigunclepostGrandyear
        self.biguncleskinCheck =biguncleskinCheck
        self.biguncleskinyear =biguncleskinyear
#ประวัติป้า
class bigAuntHistory:
    def __init__(self,accountid,optionhistorybigaunt,bigauntbreastCheck,bigauntbreastyear,bigauntliverCheck,bigauntliveryear,bigauntgutCheck,bigauntgutyear,bigauntpostGrandCheck,bigauntpostGrandyear,bigauntskinCheck,bigauntskinyear):
        self.accountid = accountid
        self.optionhistorybiguncle =optionhistorybigaunt
        self.bigauntbreastCheck =bigauntbreastCheck
        self.bigauntbreastyear = bigauntbreastyear
        self.bigauntliverCheck = bigauntliverCheck
        self.bigauntliveryear =bigauntliveryear
        self.bigauntgutCheck = bigauntgutCheck
        self.bigauntgutyear =bigauntgutyear
        self.bigauntpostGrandCheck = bigauntpostGrandCheck
        self.bigauntpostGrandyear = bigauntpostGrandyear
        self.bigauntskinCheck = bigauntskinCheck
        self.bigauntskinyear =bigauntskinyear
#ประวัติน้า
class smallAuntHistory:
    def __init__(self,accountid,optionhistorysmallaunt,smallauntbreastCheck,smallauntbreastyear,smallauntliverCheck,smallauntliveryear,smallauntgutCheck,smallauntgutyear,smallauntpostGrandCheck,smallauntpostGrandyear,smallauntskinCheck,smallauntskinyear):
        self.accountid =accountid
        self.optionhistorysmallaunt = optionhistorysmallaunt
        self.smallauntbreastCheck = smallauntbreastCheck
        self.smallauntbreastyear = smallauntbreastyear
        self.smallauntliverCheck = smallauntliverCheck
        self.smallauntliveryear = smallauntliveryear
        self,smallauntgutCheck =smallauntgutCheck
        self.smallauntgutyear =smallauntgutyear
        self.smallauntpostGrandCheck =smallauntpostGrandCheck
        self.smallautpostGrandyear =smallauntpostGrandyear
        self.smallauntskinCheck =smallauntskinCheck
        self.smallauntskinyear =smallauntskinyear
#ประวัติอา
class smallbroHistory: 
    def __init__(self,accountid,optionhistorysmallbro,smallbrobreastCheck,smallbrobreastyear,smallbroliverCheck,smallbroliveryear,smallbrogutCheck,smallbrogutyear,smallbropostGrandCheck,smallbropostGrandyear,smallbroskinCheck,smallbroskinyear):
        self.acoountid =accountid
        self.optionhistorysmallbro=optionhistorysmallbro
        self.smallbrobreastCheck=smallbrobreastCheck
        self.smallbrobreastyear = smallbrobreastyear
        self.smallbroliverCheck = smallbroliverCheck
        self.smallbroliveryear =smallbroliveryear
        self.smallbrogutCheck =smallbrogutCheck
        self.smallbrogutyear =smallbrogutyear
        self.smallbropostGrandCheck =smallbropostGrandCheck
        self.smallbropostGrandyear =smallbropostGrandyear
        self.smallbroskinCheck =smallbroskinCheck
        self.smallbroskinyear =smallbroskinyear
#ประวัติหลานชาย
class mengrandChildHistory:
    def __init__(self,accountid,optionhistorymengrandchild,mengrandChildbreastCheck,mengrandChildbreastyear,mengrandChildyear,mengrandChildliverCheck,mengrandChildliveryear,mengrandChildgutCheck,mengrandChildgutyear,mengrandChildpostGrandCheck,mengrandChildpostGrandyear,mengrandChildskinCheck,mengrandChildskinyear):
        self.accountid =accountid
        self.optionhistorymengrandchild = optionhistorymengrandchild
        self.mengrandChildbreastCheck = mengrandChildbreastCheck
        self.mengrandChildbreastyear =  mengrandChildbreastyear
        self.mengrandChildliverCheck = mengrandChildliverCheck
        self.mengrandChildliveryear = mengrandChildliveryear
        self.mengrandChildgutCheck = mengrandChildgutCheck
        self.mengrandChildgutyear =mengrandChildgutyear
        self.mengrandChildpostGrandCheck = mengrandChildpostGrandCheck
        self.mengrandChildpostGrandyear =mengrandChildpostGrandyear
        self.mengrandChildskinCheck = mengrandChildskinCheck
        self.mengrandChildskinyear = mengrandChildskinyear
#ประวัติหลานสาว
class womengrandChildHistoty:
    def __init__(self,accountid,optionhistorywomengrandchild,womengrandchildbreastCheck,womengrandchildbreastyear,womengrandchildliverCheck,womengrandchildliveryear,womengrandchildgutCheck,womengrandchildgutyear,womengrandchildpostGrandCheck,womengrandchildpostGrandyear,womengrandchildskinCheck,womengrandchildskinyear):
        self.accountid =accountid
        self.optionhistorywomengrandchild =optionhistorywomengrandchild
        self.womengrandchildbreastCheck = womengrandchildbreastCheck
        self.womengrandchildbreastyear = womengrandchildbreastyear
        self.womengrandchildliverCheck =womengrandchildliverCheck
        self.womengrandchildliveryear = womengrandchildliveryear
        self.womengrandchildgutCheck = womengrandchildgutCheck
        self.womengrandchildgutyear = womengrandchildgutyear
        self.womengrandchildpostGrandCheck= womengrandchildpostGrandCheck
        self.womengrandchildpostGrandyear = womengrandchildpostGrandyear
        self.womengrandchildskinCheck = womengrandchildskinCheck
        self.womengrandchildskinyear = womengrandchildskinyear
#ประวัติเหลนชาย
class thirdmengrandChildHistory:
    def __init__(self,accountid,optionhistorythirdmengrandchild,thirdmengrandchildbreastCheck,thirdmengrandchildbreastyear,thirdmengrandchildliverCheck,thirdmengrandchildliveryear,thirdmengrandchildgutCheck,thirdmengrandchildgutyear,thirdmengrandchildpostGrandCheck,thirdmengrandchildpostGrandyear,thirdmengrandchildskinCheck,thirdmengrandchildskinyear):
        self.accountid = accountid
        self.optionhistorythirdmengrandchild = optionhistorythirdmengrandchild
        self.thirdmengrandchildbreastCheck  = thirdmengrandchildbreastCheck
        self.thirdmengrandchildbreastyear = thirdmengrandchildbreastyear
        self.thirdmengrandchildliverCheck = thirdmengrandchildliverCheck
        self.thirdmengrandchildliveryear = thirdmengrandchildliveryear
        self.thirdmengrandchildgutCheck =thirdmengrandchildgutCheck
        self.thirdmengrandchildgutyear =thirdmengrandchildgutyear
        self.thirdmengrandchildpostGrandCheck = thirdmengrandchildpostGrandCheck
        self.thirdmengrandchildpostGrandyear  = thirdmengrandchildpostGrandyear
        self.thirdmengrandchildskinCheck = thirdmengrandchildskinCheck
        self.thirdmengrandchildskinyear = thirdmengrandchildskinyear
#ประวัติเหลนหญิง
class thirdwomendgrandChildHistory:
    def __init__(self,accountid,optionhistorythirdwomangrandchild,thirdwomangrandchildbreastCheck,thirdwomangrandchildbreastyear,thirdwomangrandchildliverCheck,thirdwomangrandchildliveryear,thirdwomangrandchildgutCheck,thirdwomangrandchildgutyear,thirdwomangrandchildpostGrandCheck,thirdwomangrandchildpostGrandyear,thirdwomangrandchildskinCheck,thirdwomangrandchildskinyear):
       self.accountid = accountid
       self.optionhistorythirdwomangrandchild =optionhistorythirdwomangrandchild
       self.thirdwomangrandchildbreastCheck = thirdwomangrandchildbreastCheck 
       self.thirdwomangrandchildbreastyear = thirdwomangrandchildbreastyear
       self.thirdwomangrandchildliverCheck = thirdwomangrandchildliverCheck
       self.thirdwomangrandchildliveryear = thirdwomangrandchildliveryear
       self.thirdwomangrandchildgutCheck = thirdwomangrandchildgutCheck
       self.thirdwomangrandchildgutyear =thirdwomangrandchildgutyear
       self.thirdwomangrandchildpostGrandCheck = thirdwomangrandchildpostGrandCheck
       self.thirdwomangrandchildpostGrandyear = thirdwomangrandchildpostGrandyear
       self.thirdwomangrandchildskinCheck = thirdwomangrandchildskinCheck
       self.thirdwomangrandchildskinyear = thirdwomangrandchildskinyear




