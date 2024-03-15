from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func


Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    # Atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship("Address", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    # Atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"

# conexão com banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# criando inspetor, que investiga o schema do database
insp = inspect(engine)
# pesquisando se existe tabela "x" no schema
print(insp.has_table("user_account"))
# pegando nome das tabelas dentro do schema
print(insp.get_table_names())
# pegando nome do schema
print(insp.default_schema_name)

# Iniciando sessão do banco de dados
with Session(engine) as session:
    # criando objeto/entidade que será persistida
    gandalf = User(
        name = "gandalf",
        fullname = "gandalf o cinzento",
        address = [Address(email_address="greygandalf@hobbit.com")]
    )
    # criando objeto/entidade que será persistida
    saruman = User(
        name = "saruman",
        fullname = "saruman o branco",
        address = [Address(email_address="whitesaruman@hobbit.com"), 
                            Address(email_address="whitesaruman@hobbit.org")]
    )
    # criando objeto/entidade que será persistida
    sam = User(
        name = "sam",
        fullname = "sam o hobbit",
    )
    # Enviando para o database 
    session.add_all([gandalf, saruman, sam])
    # comitando para persistir operação de escrita no db
    session.commit()

# definindo statement sql para retornar dados do banco de dados
stmt = select(User).where(User.name.in_(["gandalf", "saruman", "sam"]))
print("\nrecuperando os users da tabela de usuarios")
for user in session.scalars(stmt):
    print(user)

# definindo statement sql para retornar dados do banco de dados
stmt_address = select(Address).where(Address.user_id.in_([2]))
print("\nrecuperando os endereços do saruman [user_id=2]")
for address in session.scalars(stmt_address):
    print(address)

# definindo statement sql para retornar dados da tabela
stmt_order= select(User).order_by(User.fullname.desc())
print("\nrecuperando info da tabela de forma ordenada")
for result in session.scalars(stmt_order):
    print(result)

#Definindo join para retornar dados da tabela com scalars que retorna apenas o primeiro resultado.
stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
print("\nRecuperando dados de duas tabelas, através de um join")
for result in session.scalars(stmt_join):
        print(result)


#Definindo join para retornar dados da tabela atraves de uma conexão com o banco de dados.
#Desse modo o objeto retornado ao inves de usar o scalars, que retorna apenas o primeiro resultado.
#Usamos o fetchall para retornar todos os resultados.
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\n executando statement a partir da concection")
for result in results:
    print(result)


#Usando funções sql como count para retornar dados agregados da tabela.
stmt_count = (select(func.count("*")).select_from(User))
print("\nContando quantos registros existem na tabela User")
for result in session.scalars(stmt_count):
    print(result)


#encerrando session
session.close()