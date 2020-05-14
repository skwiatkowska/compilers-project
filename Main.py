from antlr4 import *
from LangLexer import LangLexer
from LangListener import LangListener  as LangBaseListener
from LangParser import LangParser
import sys


class LangVarListener(LangBaseListener):
    def enterOperator(self, ctx: LangParser.OperatorContext):
        print("", ctx.getText(), "", end='')

    def enterLogical_operator(self, ctx: LangParser.Logical_operatorContext):
        if ctx.AND():
            print(" and ")
        else:
            print(" or ")

    def enterRelation_operator(self, ctx: LangParser.Relation_operatorContext):  # added returns for logical statements
        if ctx.NOT_EQUAL():
         #   print(" != ", end='')
            return "!="
        elif ctx.EQUAL():
         #   print(" == ", end='')
            return "=="
        elif ctx.GREATER_EQ():
         #   print(" >= ", end='')
            return ">="
        elif ctx.GREATER():
         #   print(" > ", end='')
            return ">"
        elif ctx.LESS():
         #   print(" < ", end='')
            return "<"
        elif ctx.LESS_EQ():
         #   print(" <= ", end='')
            return "<="

    # def enterDeclaration(self, ctx: LangParser.Class_defContext):
    #    print(ctx.NAME().getText())

    def enterDeclaration(self, ctx:LangParser.DeclarationContext):
        return str(ctx.NAME())

    def exitDeclaration(self, ctx:LangParser.DeclarationContext):
        print()

    def enterDefinition(self, ctx: LangParser.DefinitionContext):
        child2 = 'nie ma deklaracji'

        if hasattr(ctx, "declaration"):
            child2 = self.enterDeclaration(ctx.declaration()) + "="
            def_value = self.enterAssign_val(ctx.assign_val())
            child2 += def_value
            print(child2)

        return child2

    def exitDefinition(self, ctx: LangParser.DefinitionContext):
        print("")

    def enterAssign_val(self, ctx: LangParser.Assign_valContext):
        if isinstance(ctx, LangParser.Assign_valContext):
            as_v_str = str(self.enterValue(ctx.value()))
        return as_v_str

    def enterAssignment(self, ctx: LangParser.AssignmentContext):
        #print(ctx.NAME().getText(), "= ", end='')
        assign_str = str(ctx.NAME().getText()) + "= " + 'assignment string'
        return assign_str

    def exitAssignment(self, ctx: LangParser.AssignmentContext):
        print('')

    def enterValue(self, ctx: LangParser.ValueContext):
        if ctx.STRING_VAL():  #print(ctx.STRING_VAL().getText(), end='')
            str_v = ctx.STRING_VAL()
            return str_v

        if ctx.var_or_num_value():
            n_str = str(self.enterVar_or_num_value(ctx.var_or_num_value()))
            return n_str

        if hasattr(ctx, "math_operation"):
            math_str = str(self.enterMath_operation(ctx.math_operation()))
            return math_str

        if hasattr(ctx, "fun_call"):
            func_str = str(self.enterFun_call(ctx.fun_call()))
            print('funkcja')
            return func_str







    def enterVar_or_num_value(self, ctx: LangParser.Var_or_num_valueContext):
        if(ctx.NAME()):
           # print(ctx.NAME().getText(), end='')
            #print('name')
            str_s = str(ctx.NAME())
            return str_s  #zmienic dla wszystkich
        elif ctx.INT_VAL:
            #print(ctx.INT_VAL().getText(), end='')
            return str(ctx.INT_VAL().getText())
        elif ctx.DOUBLE_VAL:
            #print(ctx.DOUBLE_VAL().getText(), end='')
            return str(ctx.DOUBLE_VAL().getText())


    def enterMath_operation(self, ctx:LangParser.Math_operationContext):
        #math_str = str(self.enterMath_operation(ctx.math_operation()))
        #print('math in math')
        print('', end='')

    def exitMath_operation(self, ctx:LangParser.Math_operationContext):
        print()

    def enterFun_call(self, ctx: LangParser.Fun_callContext):
        print(ctx.NAME().getText(), "(", end='')

    def exitFun_call(self, ctx: LangParser.Fun_callContext):
        print(")")

    def enterFun_args(self, ctx: LangParser.Fun_argsContext):
        pass

    def enterFun_params(self, ctx: LangParser.Fun_paramsContext):
        pass
        """
        for child in ctx.getChildren():
            if child != LangParser.Var_typeContext:
                if child.NAME():
                    print(child.NAME().getText(), end='')
                elif child.COMA():
                    print(",", end='')
        """

    def enterFun_declaration(self, ctx: LangParser.Fun_declarationContext):
        print(ctx.NAME().getText(), "(", end='')

    def exitFun_declaration(self, ctx: LangParser.Fun_declarationContext):
        print("):")

    def enterFun_def(self, ctx: LangParser.Fun_defContext):
        print("def ", end='')
        pass

    def enterClass_def(self, ctx: LangParser.Class_defContext):
        print("class", ctx.NAME().getText(), ":")

    def enterPrintf(self, ctx: LangParser.PrintfContext):
        print("\nprint(", end='')

    def exitPrintf(self, ctx: LangParser.PrintfContext):
        print(")")

    def enterReturn_value(self, ctx: LangParser.Return_valueContext):
        #print("\nreturn ", end='')
        return_str = "\nreturn "
        ret_value = str(self.enterValue(ctx.value()))
        return_str += ret_value
        return return_str

    def exitReturn_value(self, ctx: LangParser.Return_valueContext):
        print()

    def enterIncrement(self, ctx: LangParser.IncrementContext):
        print(ctx.NAME().getText(), "+= 1")

    def enterDecrement(self, ctx: LangParser.DecrementContext):
        print(ctx.NAME().getText(), "-= 1")


#----------------   LOGICZNE

    def enterConditions(self, ctx: LangParser.ConditionsContext):
        #print(ctx.logical_operator())  #pusta lista
        number_of_operators = 0 #len(ctx.logical_operator) - sprawdzic pozniej przez isEmpty()

        #print('(', end='')

        if (number_of_operators == 0):
            conditions = str(self.enterCondition(ctx.condition()[0]))  # to daje: 	x < None10    None (kolejny None dolaczyl)
            return conditions
        else:
            conditions = "too many conditions"
            return conditions
          #  operator_counter = 0
          #  for i in range(number_of_operators + 1):
          #      print(self.enterCondition(ctx.condition()[i]), end='')
          #      if (operator_counter!=number_of_operators):
          #          print(ctx.logical_operator()[operator_counter], end='')

    def exitConditions(self, ctx: LangParser.ConditionsContext):
        print('', end='')

    def enterCondition(self, ctx:LangParser.ConditionContext):
        variable = ctx.var_or_num_value()[0].getText()
        operatorr = self.enterRelation_operator(ctx.relation_operator())
        value = ctx.var_or_num_value()[1].getText()
        condition = variable + str(operatorr) + value
        return condition

    def exitCondition(self, ctx:LangParser.ConditionContext):
        print('', end='')

    def enterLogical_stmt(self, ctx:LangParser.Logical_stmtContext):
        logical_statement = str(self.enterConditions(ctx.conditions()))
        return logical_statement

    def exitLogical_stmt(self, ctx:LangParser.Logical_stmtContext):
        print('', end='')

    def enterBrack_logical_stm(self, ctx:LangParser.Brack_logical_stmContext):
        logical_bracket = str(self.enterLogical_stmt(ctx.logical_stmt()))
        return logical_bracket

    def exitBrack_logical_stm(self, ctx:LangParser.Brack_logical_stmContext):
        print('', end='')


#-------------------    PETLE, IF

    def enterWhile_def(self, ctx:LangParser.While_defContext):  #dziala
        while_statement = str(self.enterBrack_logical_stm(ctx.brack_logical_stm()))
        print('\nwhile (', while_statement, '):' )

    def exitWhile_def(self, ctx:LangParser.While_defContext):
        print('', end='')


    def enterFor_def(self, ctx:LangParser.For_defContext):
        print('\nfor(', ctx.NAME().getText(), 'in range(', ctx.INT_VAL()[0], ',', ctx.INT_VAL()[1],')):')

    def exitFor_def(self, ctx:LangParser.For_defContext):
        print('', end='')

    def enterIf_def(self, ctx:LangParser.If_defContext):

        if(ctx.IF()):           # zmienic logiczne statementy na poprawne:
                                #usunac nawiasy kwadratowe
            if_statement = str(self.enterBrack_logical_stm(ctx.brack_logical_stm()[0]))
            print('if(', if_statement, '): ', end='')
            print(ctx.body()[0].getText())  # [zwroc("1");]
            body1 = self.enterBody(ctx.body()[0])
            print(body1, 'body1')

        if(ctx.ELSE_IF()):
            elif_statement = str(self.enterBrack_logical_stm(ctx.brack_logical_stm()[1]))
            print('elif(', elif_statement, '):', end="")
            print(ctx.body()[1].getText())  # [zwroc("2");]
        if(ctx.ELSE()):
            print('else:')
            print(ctx.body()[2].getText())  # [zwroc("3");]


    def exitIf_def(self, ctx:LangParser.If_defContext):
        print('', end='')


# LINE, SEMI-LINE
    # Enter a parse tree produced by LangParser#line.
    def enterLine(self, ctx:LangParser.LineContext):
        list_of_lines = ctx
        if isinstance(list_of_lines, list):
            line_str=''
            for i in range(len(list_of_lines)):
                line_str += str(self.enterLine_semi(ctx[i].line_semi())) + '\n'
        else:
            line_str = str(self.enterLine_semi(ctx.line_semi()))  # tak dla wszystkich
        return line_str

    def exitLine(self, ctx:LangParser.LineContext):
        print()

    def enterLine_semi(self, ctx:LangParser.Line_semiContext):
        if hasattr(ctx, "definition"):
            func_str = str(self.enterDefinition(ctx.definition()))
            return func_str

        if hasattr(ctx, "assignment"):
            func_str = str(self.enterAssignment(ctx.assignment().getText()))
            print('assignment')
            return func_str
        if hasattr(ctx, "return_value"):
            func_str = str(self.enterFun_call(ctx.fun_call()))
            print('return_value')
            return func_str
        if hasattr(ctx, "printf"):
            func_str = str(self.enterFun_call(ctx.fun_call()))
            print('printf')
            return func_str
        if hasattr(ctx, "fun_call"):
            func_str = str(self.enterFun_call(ctx.fun_call()))
            print('funkcja')
            return func_str
        if hasattr(ctx, "increment"):
            func_str = str(self.enterFun_call(ctx.fun_call()))
            print('increment')
            return func_str

        return 'return z semi line'

    def exitLine_semi(self, ctx:LangParser.Line_semiContext):
        print('  ')



#-------------------- BODY

    def enterBody(self, ctx:LangParser.BodyContext):
      #  print('    ', end='')   #robi TAB w ciele funkcji w pierwszej linijce
        body_str = str(self.enterLine(ctx.line()))
        return body_str

    def exitBody(self, ctx:LangParser.BodyContext):
        print('', end= '')



# ---------------------  CODE
    def enterCode(self, ctx:LangParser.CodeContext):
        #print('    ', end='')   #robi TAB przed atrybutami klasy i definicjami funkcji klasy
        print()

    # Exit a parse tree produced by LangParser#code.
    def exitCode(self, ctx:LangParser.CodeContext):
        print('', end='')


    # Enter a parse tree produced by LangParser#main.
    def enterMain(self, ctx:LangParser.MainContext):
        print('main(): ')

    # Exit a parse tree produced by LangParser#main.
    def exitMain(self, ctx:LangParser.MainContext):
        print()



def main():
    input_stream = FileStream("test1.txt")  # sys.argv[1])
    lexer = LangLexer(input_stream)
    # lexer = LangLexer(StdinStream())
    tokens = CommonTokenStream(lexer)
    parser = LangParser(tokens)

    tree = parser.class_def()
    listener = LangVarListener()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    main()