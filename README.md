# SISAP - Asistencias Red Salud

source venv/bin/activate

## Credenciales

### Credenciales de producción

```bash s

FLASK_ENV="production"

DATABASE_URI="mysql+pymysql://rsaws2019:prS$$*20Hcars@rsheaddbrds20.czvvckkesgis.us-east-2.rds.amazonaws.com:3306/new_redes_peru"
SEC_DATABASE_URI="mysql+pymysql://rsaws2019:prS$$*20Hcars@rsheaddbrds20.czvvckkesgis.us-east-2.rds.amazonaws.com:3306/db_usuarios"

DB_HOST="rsheaddbrds20.czvvckkesgis.us-east-2.rds.amazonaws.com"
DB_NAME="new_redes_peru"
DB_USER="rsaws2019"
DB_PASS="prS$$*20Hcars"

AWS_ACCOUNT_ID="720586246653"
AWS_BUCKET_NAME="asistencias-redsalud"
AWS_BUCKET_NAME_RECURSOS="red-salud"

EMAIL_SMTP="email-smtp.us-east-1.amazonaws.com"
EMAIL_PORT="587"
EMAIL_USER="AKIA2PRSJRH6UBJ7J6OH"
EMAIL_PASS="BH5ySduLgjqkgq2venaB6R5ErdVrXvLfTHnbcusiP3w0"

```

### Credenciales de desarrollo

```bash

FLASK_ENV="development"

DATABASE_URI="mysql+pymysql://rsdevus1:developer2020RS#$1@rdsdevenv.czvvckkesgis.us-east-2.rds.amazonaws.com/new_redes_peru"
SEC_DATABASE_URI="mysql+pymysql://rsdevus1:developer2020RS#$1@rdsdevenv.czvvckkesgis.us-east-2.rds.amazonaws.com/db_usuarios"

DB_HOST="rsheaddbrds20.czvvckkesgis.us-east-2.rds.amazonaws.com"
DB_NAME="new_redes_peru"
DB_USER="rsaws2019"
DB_PASS="prS$$*20Hcars"

AWS_ACCOUNT_ID="720586246653"
AWS_BUCKET_NAME="asistencias-redsalud"
AWS_BUCKET_NAME_RECURSOS="red-salud"

EMAIL_SMTP="email-smtp.us-east-1.amazonaws.com"
EMAIL_PORT="587"
EMAIL_USER="AKIA2PRSJRH6UBJ7J6OH"
EMAIL_PASS="BH5ySduLgjqkgq2venaB6R5ErdVrXvLfTHnbcusiP3w0"

```