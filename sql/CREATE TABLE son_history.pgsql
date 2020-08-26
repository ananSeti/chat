--ประวัติลูกชาย
CREATE TABLE son_history(
id SERIAL PRIMARY KEY,
sonHistoryId INTEGER not NULL,
optionhistoryson INTEGER , /* 0. ไม่เป็น  1.เป็น*/
sonbreastcheck INTEGER,
sonbreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
sonliverCheck INTEGER, /*มะเร็งตับอ่อน*/
sonliveryear INTEGER, /*ปีที่เป็น*/
songutCheck INTEGER,
songutyear INTEGER,
sonpostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
sonpostGrandYear INTEGER, /* ปีที่เป็น*/
sonskinCheck  INTEGER, /*มะเร็งผิวหนัง */
sonskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(sonHistoryId) REFERENCES a_user(id)
);

--ประวัติลูกสาว
CREATE TABLE daughter_history(
id SERIAL PRIMARY KEY,
daughterHistoryId INTEGER not NULL,
optionhistorydaughter INTEGER , /* 0. ไม่เป็น  1.เป็น*/
daughterbreastCheck INTEGER,
daughterbreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
daughterliverCheck INTEGER, /*มะเร็งตับอ่อน*/
daughterliveryear INTEGER, /*ปีที่เป็น*/
daughtergutcheck INTEGER,
daughtergutyear INTEGER,
daughterpostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
daughterpostGrandyear INTEGER, /* ปีที่เป็น*/
daughterskinChek  INTEGER, /*มะเร็งผิวหนัง */
daughterskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(daughterHistoryId) REFERENCES a_user(id)
);
--ประวัติพ่อ
CREATE TABLE father_history(
id SERIAL PRIMARY KEY,
fatherHistoryId INTEGER not NULL,
optionhistoryfather INTEGER , /* 0. ไม่เป็น  1.เป็น*/
fatherbreatCheck INTEGER,
fatherbreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
fatherliverCheck INTEGER, /*มะเร็งตับอ่อน*/
fatherliveryear INTEGER, /*ปีที่เป็น*/
fathergutCheck INTEGER,
fathergutyear INTEGER,
fatherpostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
fartherpostGrandyear INTEGER, /* ปีที่เป็น*/
fatherskinCheck  INTEGER, /*มะเร็งผิวหนัง */
fatherskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(fatherHistoryId) REFERENCES a_user(id) 
); 
--ประวัติแม่
CREATE TABLE mother_history(
id SERIAL PRIMARY KEY,
motherHistoryId INTEGER not NULL,
optionhistorymother INTEGER , /* 0. ไม่เป็น  1.เป็น*/
motherbreastCheck INTEGER,
motherbreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
motherliverCheck INTEGER, /*มะเร็งตับอ่อน*/
motherliveryear INTEGER, /*ปีที่เป็น*/
mothergutCheck INTEGER,
mothergutyear INTEGER,
motherpostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
motherpostGrandyear INTEGER, /* ปีที่เป็น*/
motherskinCheck  INTEGER, /*มะเร็งผิวหนัง */
motherskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(motherHistoryId) REFERENCES a_user(id) 
); 
--ประวัติน้องชาย
CREATE TABLE  brother_history(
id SERIAL PRIMARY KEY,
brotherHistoryId INTEGER not NULL,
optionhistorylbrother INTEGER , /* 0. ไม่เป็น  1.เป็น*/
brotherbreastCheck INTEGER,
brotherbreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
brotherlivercheck INTEGER, /*มะเร็งตับอ่อน*/
brotherliveryear INTEGER, /*ปีที่เป็น*/
brothergutCheck INTEGER,
brothergutyear INTEGER,
brotherpostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
brotherpostGrandyear INTEGER, /* ปีที่เป็น*/
brotherskinCheck  INTEGER, /*มะเร็งผิวหนัง */
brotherskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(brotherHistoryId) REFERENCES a_user(id) 
); 
--ประวัติน้องหญิง
CREATE TABLE  sister_history(
id SERIAL PRIMARY KEY,
sisterHistoryId INTEGER not NULL,
optionhistorysister INTEGER , /* 0. ไม่เป็น  1.เป็น*/
sisterbreastCheck INTEGER,
sisterbreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
sisterliverCheck INTEGER, /*มะเร็งตับอ่อน*/
sisterliveryear INTEGER, /*ปีที่เป็น*/
sistergutCheck INTEGER,
sistergutyear INTEGER,
sisterpostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
sisterpostGrandyear INTEGER, /* ปีที่เป็น*/
sisterskinCheck  INTEGER, /*มะเร็งผิวหนัง */
sisterskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(sisterHistoryId) REFERENCES a_user(id) 
); 
--ประวัติทวดชาย
CREATE TABLE mangrandFa_history(
id SERIAL PRIMARY KEY,
mangrandFaHistoryId INTEGER not NULL,
optionhistorymangrandfather INTEGER , /* 0. ไม่เป็น  1.เป็น*/
mangrandFabreastCheck INTEGER,
mangrandFabreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
mangrandFaliverCheck INTEGER, /*มะเร็งตับอ่อน*/
mangrandFaliveryear INTEGER, /*ปีที่เป็น*/
mangrandFagutCheck INTEGER,
mangrandFagutyear INTEGER,
mangrandFapostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
mangrandFapostGrandyear INTEGER, /* ปีที่เป็น*/
mangrandFaskinCheck  INTEGER, /*มะเร็งผิวหนัง */
mangrandFaskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(mangrandFaHistoryId) REFERENCES a_user(id) 
); 
-- ประวัติทวดหญิง
CREATE TABLE womangrandMom_history(
id SERIAL PRIMARY KEY,
womangrandMomHistoryId INTEGER not NULL,
optionhistorywomangrandmother INTEGER , /* 0. ไม่เป็น  1.เป็น*/
womangrandMomCheck INTEGER,
womangrandMomyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
womangrandMomliverCheck INTEGER, /*มะเร็งตับอ่อน*/
womangrandMomliveryear INTEGER, /*ปีที่เป็น*/
womandgrandgutCheck INTEGER,
womangrandgutyear INTEGER,
womangrandpostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
womangrandpostGrandyear INTEGER, /* ปีที่เป็น*/
womangrandskinCheck  INTEGER, /*มะเร็งผิวหนัง */
womangrandskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(womangrandMomHistoryId) REFERENCES a_user(id) 
); 
--ประวัติปู่
CREATE TABLE grandFather_history(
id SERIAL PRIMARY KEY,
grandFatherHistoryId INTEGER not NULL,
optionhistorygrandfather INTEGER , /* 0. ไม่เป็น  1.เป็น*/
grandFatherbreastCheck INTEGER,
grandFatherbreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
grandFartherliverCheck INTEGER, /*มะเร็งตับอ่อน*/
grandFatherliveryear INTEGER, /*ปีที่เป็น*/
grandFathergutCheck INTEGER,
granFathergutyear INTEGER,
grandFatherpostgrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
grandFatherpostGrandyear INTEGER, /* ปีที่เป็น*/
grandFatherskinsCheck  INTEGER, /*มะเร็งผิวหนัง */
grandFatherskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(grandFatherHistoryId) REFERENCES a_user(id) 
); 
--ประวัติย่า
CREATE TABLE grandMom_history(
id SERIAL PRIMARY KEY,
grandMomHistoryId INTEGER not NULL,
optionhistorygrandmother INTEGER , /* 0. ไม่เป็น  1.เป็น*/
grandMombreastCheck INTEGER,
grandMombreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
grandMomliverCheck INTEGER, /*มะเร็งตับอ่อน*/
grandMomliveryear INTEGER, /*ปีที่เป็น*/
grandMomgutCheck INTEGER,
grandMomgutyear INTEGER,
grandMompostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
grandMompostGrandyear INTEGER, /* ปีที่เป็น*/
grandMomskinCheck  INTEGER, /*มะเร็งผิวหนัง */
grandMomskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(grandMomHistoryId) REFERENCES a_user(id) 
); 
--ประวัติตา
CREATE TABLE fatherOfMom_history(
id SERIAL PRIMARY KEY,
fatherOfMomHistoryId INTEGER not NULL,
optionhistoryfathermom INTEGER , /* 0. ไม่เป็น  1.เป็น*/
fatherOfMombreastCheck INTEGER,
fatherOfMombreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
fatherOfMomliverCheck INTEGER, /*มะเร็งตับอ่อน*/
fatherOfMomliveryear INTEGER, /*ปีที่เป็น*/
fatherOfMomgutCheck INTEGER,
fatherOfMomgutyear INTEGER,
fatherOfMompostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
fatherOfMompostGrandyear INTEGER, /* ปีที่เป็น*/
fatherOfMomskinCheck  INTEGER, /*มะเร็งผิวหนัง */
fatherOfMomskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(fatherOfMomHistoryId) REFERENCES a_user(id) 
); 
 --ประวัติยาย
CREATE TABLE motherOfMom_history(
id SERIAL PRIMARY KEY,
mohterOfMomHistoryId INTEGER not NULL,
optonhistorymothermom INTEGER , /* 0. ไม่เป็น  1.เป็น*/
motherOfMombreastCheck INTEGER,
motherOfMombreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
motherOfMomliverCheck INTEGER, /*มะเร็งตับอ่อน*/
motherOfMomliveryear INTEGER, /*ปีที่เป็น*/
motherOfMomgutCheck INTEGER,
motherOfMomgutyear INTEGER,
motherOfMompostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
motherOfMompostGrandyear INTEGER, /* ปีที่เป็น*/
motherOfMomskinCheck  INTEGER, /*มะเร็งผิวหนัง */
motherOfMomskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(mohterOfMomHistoryId) REFERENCES a_user(id) 
); 
-- ประวัติลุง
CREATE TABLE bigUncle_history(
id SERIAL PRIMARY KEY,
bigUncleHistoryId INTEGER not NULL,
optionhistorybiguncle INTEGER , /* 0. ไม่เป็น  1.เป็น*/
bigunclebreastCheck INTEGER,
bigunclebreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
biguncleliverCheck INTEGER, /*มะเร็งตับอ่อน*/
biguncleliveryear INTEGER, /*ปีที่เป็น*/
bigunclegutCheck INTEGER,
bigunclegutyear INTEGER,
bigunclepostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
bigunclepsotGrandyear INTEGER, /* ปีที่เป็น*/
biguncleskinCheck  INTEGER, /*มะเร็งผิวหนัง */
biguncleskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(bigUncleHistoryId) REFERENCES a_user(id) 
); 
--ประวัติป้า
CREATE TABLE bigAunt_history(
id SERIAL PRIMARY KEY,
bigAuntHistoryId INTEGER not NULL,
optionhistorybiguncle INTEGER , /* 0. ไม่เป็น  1.เป็น*/
bigauntbreastyear INTEGER,
bigunclebreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
bigauntliverCheck INTEGER, /*มะเร็งตับอ่อน*/
bigauntliveryear INTEGER, /*ปีที่เป็น*/
bigauntgutCheck INTEGER,
bigauntgutyear INTEGER,
bigauntpostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
bigauntpostGrandyear INTEGER, /* ปีที่เป็น*/
bigauntskinCheck  INTEGER, /*มะเร็งผิวหนัง */
bigauntskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(bigAuntHistoryId) REFERENCES a_user(id) 
); 
--ประวัติน้า
CREATE TABLE smallAunt_history(
id SERIAL PRIMARY KEY,
smallAuntHistoryId INTEGER not NULL,
optionhistorysmallaunt INTEGER , /* 0. ไม่เป็น  1.เป็น*/
smallauntbreastCheck INTEGER,
smallauntbreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
smallauntliverCheck INTEGER, /*มะเร็งตับอ่อน*/
smallauntliveryear INTEGER, /*ปีที่เป็น*/
smallauntgutCheck INTEGER,
smallauntgutyear INTEGER,
smallauntpostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
smallauntpostGrandyear INTEGER, /* ปีที่เป็น*/
smallauntskinCheck  INTEGER, /*มะเร็งผิวหนัง */
smallauntskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(smallAuntHistoryId) REFERENCES a_user(id) 
); 
--ประวัติอา
CREATE TABLE smallbro_history(
id SERIAL PRIMARY KEY,
smallbroHistoryId INTEGER not NULL,
optionhistorysmallbro INTEGER , /* 0. ไม่เป็น  1.เป็น*/
smallbrobreastCheck INTEGER,
smallbrobreastyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
smallbroliverCheck INTEGER, /*มะเร็งตับอ่อน*/
smallbroliveryear INTEGER, /*ปีที่เป็น*/
smallbrogutCheck INTEGER,
smallbrogutyear INTEGER,
smallbropostGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
smallbropostGrandyear INTEGER, /* ปีที่เป็น*/
smallbroskinCheck  INTEGER, /*มะเร็งผิวหนัง */
smallbroskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(smallbroHistoryId) REFERENCES a_user(id) 
); 
--ประวัติหลานชาย
CREATE TABLE mengrandChild_history(
id SERIAL PRIMARY KEY,
mengrandChildHistoryId INTEGER not NULL,
optionhistorymengrandchild INTEGER , /* 0. ไม่เป็น  1.เป็น*/
mengrandChildbreastCheck INTEGER,
mengrandChildyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
mengrandChildliverCheck INTEGER, /*มะเร็งตับอ่อน*/
mengrandChildliveryear INTEGER, /*ปีที่เป็น*/
mengrandChildgutCheck INTEGER,
mengrandChildgutyear INTEGER,
mengrandChildGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
mengrandChildpostGrandyear INTEGER, /* ปีที่เป็น*/
mengrandChildskinCheck  INTEGER, /*มะเร็งผิวหนัง */
mengrandChildskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(mengrandChildHistoryId) REFERENCES a_user(id) 
); 
--ประวัติหลานสาว
CREATE TABLE womangrandChild_history(
id SERIAL PRIMARY KEY,
womangrandChildHistoryId INTEGER not NULL,
optionhistorywomengrandchild INTEGER , /* 0. ไม่เป็น  1.เป็น*/
womengrandChildbreastCheck INTEGER,
womengrandChildyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
womengrandChildliverCheck INTEGER, /*มะเร็งตับอ่อน*/
womengrandChildliveryear INTEGER, /*ปีที่เป็น*/
womengrandChildgutCheck INTEGER,
womengrandChildgutyear INTEGER,
womengrandChildGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
womengrandChildpostGrandyear INTEGER, /* ปีที่เป็น*/
womengrandChildskinCheck  INTEGER, /*มะเร็งผิวหนัง */
womengrandChildskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(womangrandChildHistoryId) REFERENCES a_user(id) 
); 
--ประวัติเหลนชาย
CREATE TABLE thirdmengrandChild_history(
id SERIAL PRIMARY KEY,
thirdmengrandChildHistoryId INTEGER not NULL,
optionhistorythirdmengrandchild INTEGER , /* 0. ไม่เป็น  1.เป็น*/
thirdmengrandChildbreastCheck INTEGER,
thirdmengrandChildyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
thirdmengrandChildliverCheck INTEGER, /*มะเร็งตับอ่อน*/
thirdmengrandChildliveryear INTEGER, /*ปีที่เป็น*/
thirdmengrandChildgutCheck INTEGER,
thirdmengrandChildgutyear INTEGER,
thirdmengrandChildGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
thirdmengrandChildpostGrandyear INTEGER, /* ปีที่เป็น*/
thirdmengrandChildskinCheck  INTEGER, /*มะเร็งผิวหนัง */
thirdmengrandChildskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(thirdmengrandChildHistoryId) REFERENCES a_user(id) 
); 
--ประวัติเหลนหญิง
CREATE TABLE thirdwomangrandChild_history(
id SERIAL PRIMARY KEY,
thirdwomangrandChildHistoryId INTEGER not NULL,
optionhistorythirdwomangrandchild INTEGER , /* 0. ไม่เป็น  1.เป็น*/
thirdwomangrandChildbreastCheck INTEGER,
thirdwomangrandChildyear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
--bovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
--bovalYear INTEGER,
thirdwomangrandChildliverCheck INTEGER, /*มะเร็งตับอ่อน*/
thirdwomangrandChildliveryear INTEGER, /*ปีที่เป็น*/
thirdwomangrandChildgutCheck INTEGER,
thirdwomangrandChildgutyear INTEGER,
thirdwomangrandChildGrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
thirdwomangrandChildpostGrandyear INTEGER, /* ปีที่เป็น*/
thirdwomangrandChildskinCheck  INTEGER, /*มะเร็งผิวหนัง */
thirdwomangrandChildskinyear INTEGER, /*ปีที่เป็น */
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(thirdwomangrandChildHistoryId) REFERENCES a_user(id) 
); 
