from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String 
from sqlalchemy import ForeignKey
from sqlalchemy import text

#criando a engine do banco de dados
engine = create_engine('sqlite:///:memory')

#criando o schema do banco de dados
metadata_obj = MetaData()

#criando tabela para o schema
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)

#criando tabela para o schema
user = Table(
    'user_prefs',metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

#visualizando as tabelas que estão no schema
for table in metadata_obj.sorted_tables:
    print(table)

#criando tudo no banco de dados para persistencia
metadata_obj.create_all(engine)

#inserindo informações na tabela users
sql_insert = text("insert into user values(1, 'heitor', 'heitor.cesarino@gmail.com', 'hector')")
engine.execute(sql_insert)

#criando outro schema do bnanco de dados
metadata_obj_bank = MetaData()

#criando tabela para o schema
financial_info = Table(
    'financial_info',
    metadata_obj_bank,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)
print(financial_info.primary_key)


