BEGIN;
CREATE TABLE "usuario_usuario" (
    "id" integer NOT NULL PRIMARY KEY,
    "nome" varchar(200) NOT NULL,
    "email" varchar(200) NOT NULL,
    "senha" varchar(200) NOT NULL,
    "idade" varchar(200) NOT NULL,
    "profissao" varchar(200) NOT NULL,
    "salario" varchar(200) NOT NULL
)
;

COMMIT;
