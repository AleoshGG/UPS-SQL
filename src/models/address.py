from sqlalchemy.types import UserDefinedType

class Address(UserDefinedType):
    def get_col_spec(self):
        return "address"

    def bind_processor(self, dialect):
        def process(value):
            if value is not None:
                # Usar formateo manual para asegurarse de que no hay comillas adicionales
                state = value['state']
                locality = value['locality']
                distrit = value['distrit']
                postal_code = value['postal_code']
                
                # Evita las comillas escapadas
                return f'({state}, {locality}, {distrit}, {postal_code})'
            return None
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is not None:
                # Eliminar los paréntesis inicial y final y dividir por comas
                state, locality, distrit, postal_code = value[1:-1].split(",")
                return {
                    "state": state.strip().strip('"'),
                    "locality": locality.strip().strip('"'),
                    "distrit": distrit.strip().strip('"'),
                    "postal_code": postal_code.strip().strip('"')
                }
            return None
        return process
