/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     23.10.2019 22:02:45                          */
/*==============================================================*/


drop index "Vacancy Has Many Criteria_FK";

drop index Criterion_PK;

drop table Criterion;

drop index "One User Has Many Skills_FK";

drop index Skill_PK;

drop table Skill;

drop index User_PK;

drop table "User";

drop index "One User Has Many Vacancies_FK";

drop index Vacancy_PK;

drop table Vacancy;

/*==============================================================*/
/* Table: Criterion                                             */
/*==============================================================*/
create table Criterion (
   criterion_name       VARCHAR(20)          not null,
   vacancy_company      VARCHAR(20)          null,
   vacancy_name         VARCHAR(30)          null,
   constraint PK_CRITERION primary key (criterion_name)
);

/*==============================================================*/
/* Index: Criterion_PK                                          */
/*==============================================================*/
create unique index Criterion_PK on Criterion (
criterion_name
);

/*==============================================================*/
/* Index: "Vacancy Has Many Criteria_FK"                        */
/*==============================================================*/
create  index "Vacancy Has Many Criteria_FK" on Criterion (
vacancy_company,
vacancy_name
);

/*==============================================================*/
/* Table: Skill                                                 */
/*==============================================================*/
create table Skill (
   skill_name           VARCHAR(20)          not null,
   user_email           VARCHAR(20)          null,
   constraint PK_SKILL primary key (skill_name)
);

/*==============================================================*/
/* Index: Skill_PK                                              */
/*==============================================================*/
create unique index Skill_PK on Skill (
skill_name
);

/*==============================================================*/
/* Index: "One User Has Many Skills_FK"                         */
/*==============================================================*/
create  index "One User Has Many Skills_FK" on Skill (
user_email
);

/*==============================================================*/
/* Table: "User"                                                */
/*==============================================================*/
create table "User" (
   user_email           VARCHAR(20)          not null,
   user_name            VARCHAR(20)          null,
   user_phone           VARCHAR(15)          null,
   user_birthday        DATE                 null,
   user_location        VARCHAR(30)          null,
   user_employment      VARCHAR(15)          null,
   constraint PK_USER primary key (user_email)
);

/*==============================================================*/
/* Index: User_PK                                               */
/*==============================================================*/
create unique index User_PK on "User" (
user_email
);

/*==============================================================*/
/* Table: Vacancy                                               */
/*==============================================================*/
create table Vacancy (
   vacancy_company      VARCHAR(20)          not null,
   vacancy_name         VARCHAR(30)          not null,
   user_email           VARCHAR(20)          null,
   vacancy_location     VARCHAR(30)          null,
   vacancy_employment   VARCHAR(15)          null,
   vacancy_salary       NUMERIC(10)          null,
   constraint PK_VACANCY primary key (vacancy_company, vacancy_name)
);

/*==============================================================*/
/* Index: Vacancy_PK                                            */
/*==============================================================*/
create unique index Vacancy_PK on Vacancy (
vacancy_company,
vacancy_name
);

/*==============================================================*/
/* Index: "One User Has Many Vacancies_FK"                      */
/*==============================================================*/
create  index "One User Has Many Vacancies_FK" on Vacancy (
user_email
);

alter table Criterion
   add constraint "FK_CRITERIO_ONE VACAN_VACANCY" foreign key (vacancy_company, vacancy_name)
      references Vacancy (vacancy_company, vacancy_name)
      on delete restrict on update restrict;

alter table Skill
   add constraint "FK_SKILL_ONE USER _USER" foreign key (user_email)
      references "User" (user_email)
      on delete restrict on update restrict;

alter table Vacancy
   add constraint "FK_VACANCY_ONE USER _USER" foreign key (user_email)
      references "User" (user_email)
      on delete restrict on update restrict;

