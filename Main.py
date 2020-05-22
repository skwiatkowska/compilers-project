from antlr4 import *
from LangLexer import LangLexer
from LangListener import LangListener  as LangBaseListener
from LangParser import LangParser

import sys


class LangVarListener(LangBaseListener):

    tab = 0
    def enterOperator(self, ctx: LangParser.OperatorContext):
        return ctx.getText()

    def enterLogical_operator(self, ctx: LangParser.Logical_operatorContext):
        if ctx.AND():
            return " and "
        else:
            return " or "

    def enterRelation_operator(self, ctx: LangParser.Relation_operatorContext):  # added returns for logical statements
        if ctx.NOT_EQUAL():
            return "!="
        elif ctx.EQUAL():
            return "=="
        elif ctx.GREATER_EQ():
            return ">="
        elif ctx.GREATER():
            return ">"
        elif ctx.LESS():
            return "<"
        elif ctx.LESS_EQ():
            return "<="


    def enterDeclaration(self, ctx:LangParser.DeclarationContext):
        return str(ctx.NAME().getText())

    def exitDeclaration(self, ctx:LangParser.DeclarationContext):
        pass


    def enterDefinition(self, ctx: LangParser.DefinitionContext):
        name = self.enterDeclaration(ctx.getChild(0))
        val = self.enterAssign_val(ctx.getChild(1))
        return name+" = "+val

    def exitDefinition(self, ctx: LangParser.DefinitionContext):
        pass


    def enterAssign_val(self, ctx: LangParser.Assign_valContext):
        val = ctx.getChild(1)
        as_val = str(self.enterValue(val))
        return as_val

    def enterAssignment(self, ctx: LangParser.AssignmentContext):
        assign_str = str(ctx.NAME().getText()) + " = " + self.enterAssign_val(ctx.getChild(1))
        return assign_str

    def exitAssignment(self, ctx: LangParser.AssignmentContext):
        pass



    def enterValue(self, ctx: LangParser.ValueContext):
        child = ctx.getChild(0)
        if isinstance(child, LangParser.Var_or_num_valueContext):
            n_str = str(self.enterVar_or_num_value(child))
            return n_str
        elif isinstance(child, LangParser.Math_operationContext):
            math_str = str(self.enterMath_operation(child))
            return math_str
        elif isinstance(child, LangParser.Fun_callContext):
            func_str = str(self.enterFun_call(ctx.fun_call()))
            return func_str
        else:
            str_v = child.getText()
            return str_v

    def enterVar_or_num_value(self, ctx: LangParser.Var_or_num_valueContext):
        child = ctx.getChild(0)
        str = child.getText()
        return str


    def enterMath_operation(self, ctx:LangParser.Math_operationContext):
        if ctx != None:
            children = ctx.getChildren()
            operation = []
            for child in children:
                if isinstance(child,LangParser.Math_operationContext):
                    operation.append(self.enterMath_operation(child))
                elif isinstance(child,LangParser.OperatorContext):
                    operation.append(self.enterOperator(child))
                elif isinstance(child,LangParser.Var_or_num_valueContext):
                    operation.append(self.enterVar_or_num_value(child))
                else:
                    operation.append(child.getText())
            return ' '.join(operation)


    def exitMath_operation(self, ctx:LangParser.Math_operationContext):
        pass



# ----------------   FUNKCJA

    def enterFun_call(self, ctx: LangParser.Fun_callContext):
        name = ctx.NAME().getText()
        fun_args = ""
        if ctx.fun_args():
            fun_args = self.enterFun_args(ctx.getChild(2))
        call = name + "(" + fun_args + ")"
        return call

    def exitFun_call(self, ctx: LangParser.Fun_callContext):
        pass

    def enterFun_args(self, ctx: LangParser.Fun_argsContext):
        args = []
        children = ctx.getChildren()
        for child in children:
            if isinstance(child, LangParser.ValueContext):
                args.append(str(self.enterValue(child)))
            else:
                args.append(",")
        return ''.join(args)

    def enterFun_params(self, ctx: LangParser.Fun_paramsContext):
        params = []
        children = ctx.getChildren()
        for child in children:
            if not isinstance(child, LangParser.Var_typeContext):
                params.append(child.getText())
        return params


    def enterFun_declaration(self, ctx: LangParser.Fun_declarationContext):
        name = ctx.NAME().getText()
        params = ""
        children = ctx.getChildren()
        for child in children:
            if isinstance(child,LangParser.Fun_paramsContext):
                params = self.enterFun_params(child)
        return [name,''.join(params)]

    def exitFun_declaration(self, ctx: LangParser.Fun_declarationContext):
        pass


    def enterFun_def(self, ctx: LangParser.Fun_defContext):
        dec = self.enterFun_declaration(ctx.getChild(0))
        print("def "+dec[0]+"("+dec[1]+"):")
        body = self.enterBody(ctx.getChild(1))
        print(body)


    def enterClass_def(self, ctx: LangParser.Class_defContext):
        print("class", ctx.NAME().getText()+":")

    def enterPrintf(self, ctx: LangParser.PrintfContext):
        val = self.enterValue(ctx.getChild(2))
        prt = "print(" + val + ")"
        return prt

    def exitPrintf(self, ctx: LangParser.PrintfContext):
        pass

    def enterReturn_value(self, ctx: LangParser.Return_valueContext):
        return_str = "return "
        ret_value = str(self.enterValue(ctx.value()))
        return_str += ret_value
        return return_str

    def exitReturn_value(self, ctx: LangParser.Return_valueContext):
        pass

    def enterIncrement(self, ctx: LangParser.IncrementContext):
        inc = ctx.NAME().getText() + " += 1"
        return inc

    def enterDecrement(self, ctx: LangParser.DecrementContext):
        dec = ctx.NAME().getText() + " -= 1"
        return dec

#----------------   LOGICZNE

    def enterConditions(self, ctx: LangParser.ConditionsContext):
        children = ctx.getChildren()
        conditions = []
        for child in children:
            if isinstance(child,LangParser.ConditionContext):
                conditions.append(str(self.enterCondition(child)))
            elif isinstance(child,LangParser.Logical_operatorContext):
                conditions.append(str(self.enterLogical_operator(child)))
        return ''.join(conditions)


    def exitConditions(self, ctx: LangParser.ConditionsContext):
        pass

    def enterCondition(self, ctx:LangParser.ConditionContext):
        variable = ctx.var_or_num_value()[0].getText()
        operatorr = self.enterRelation_operator(ctx.relation_operator())
        value = ctx.var_or_num_value()[1].getText()
        condition = variable + " " + str(operatorr) + " " + value
        return condition

    def exitCondition(self, ctx:LangParser.ConditionContext):
        pass

    def enterLogical_stmt(self, ctx:LangParser.Logical_stmtContext):
        logical_statement = str(self.enterConditions(ctx.conditions()))
        return logical_statement

    def exitLogical_stmt(self, ctx:LangParser.Logical_stmtContext):
        pass

    def enterBrack_logical_stm(self, ctx:LangParser.Brack_logical_stmContext):
        logical_bracket = str(self.enterLogical_stmt(ctx.logical_stmt()))
        return logical_bracket

    def exitBrack_logical_stm(self, ctx:LangParser.Brack_logical_stmContext):
        pass


#-------------------    PETLE, IF

    def enterWhile_def(self, ctx:LangParser.While_defContext):  #dziala
        while_statement = str(self.enterBrack_logical_stm(ctx.brack_logical_stm()))
        #print('while', while_statement + ':')
        body = self.enterBody(ctx.body())
        return ''.join(['while ', while_statement, ':\n',body])

    def exitWhile_def(self, ctx:LangParser.While_defContext):
        pass


    def enterFor_def(self, ctx:LangParser.For_defContext):
        statement = 'for '+ ctx.NAME().getText() + ' in range('+str(ctx.INT_VAL()[0])+','+str(ctx.INT_VAL()[1])+'):\n'
        body = self.enterBody(ctx.body())
        #print(body)
        return ''.join([statement,body])

    def exitFor_def(self, ctx:LangParser.For_defContext):
        pass


    def enterIf_def(self, ctx:LangParser.If_defContext):
        children = ctx.getChildren()
        df = []
        for child in children:
            if isinstance(child, LangParser.Brack_logical_stmContext):
                statement = str(self.enterBrack_logical_stm(child))
                df.append(statement+':\n')
            elif isinstance(child, LangParser.BodyContext):
                body = self.enterBody(child)
                df.append(body)
            else:
                text = child.getText()
                if text == 'jezeli':
                    df.append("if ")
                elif text == 'inaczejJezeli':
                    df.append("\t"*tab+"elif ")
                else:
                    df.append("\t"*tab+"else:\n")
        return ''.join(df)

    def exitIf_def(self, ctx:LangParser.If_defContext):
        pass


# LINE, SEMI-LINE
    # Enter a parse tree produced by LangParser#line.
    def enterLine(self, ctx:LangParser.LineContext):
        child = ctx.getChild(0)
        if isinstance(child, LangParser.Line_semiContext):
            line_str = str(self.enterLine_semi(child))
            return line_str
        elif isinstance(child, LangParser.If_defContext):
            line_str = str(self.enterIf_def(child))
            return line_str
        elif isinstance(child, LangParser.For_defContext):
            line_str = str(self.enterFor_def(child))
            return line_str
        elif isinstance(child, LangParser.While_defContext):
            line_str = str(self.enterWhile_def(child))
            return line_str
        else:
            return "\t"

    def exitLine(self, ctx:LangParser.LineContext):
        pass

    def enterLine_semi(self, ctx:LangParser.Line_semiContext):
        if ctx != None:
            line = ctx.getChild(0)
            if isinstance(line, LangParser.DeclarationContext):
                func_str = str(self.enterDeclaration(line))
                return func_str
            elif isinstance(line, LangParser.DefinitionContext):
                func_str = str(self.enterDefinition(line))
                return func_str
            elif isinstance(line, LangParser.AssignmentContext):
                func_str = str(self.enterAssignment(line))
                return func_str
            elif isinstance(line, LangParser.Return_valueContext):
                func_str = str(self.enterReturn_value(line))
                return func_str
            elif isinstance(line, LangParser.PrintfContext):
                func_str = str(self.enterPrintf(line))
                return func_str
            elif isinstance(line, LangParser.Fun_callContext):
                func_str = str(self.enterFun_call(line))
                return func_str
            elif isinstance(line, LangParser.IncrementContext):
                func_str = str(self.enterIncrement(line))
                return func_str
            elif isinstance(line, LangParser.DecrementContext):
                func_str = str(self.enterDecrement(line))
                return func_str


    def exitLine_semi(self, ctx:LangParser.Line_semiContext):
        pass



#-------------------- BODY

    def enterBody(self, ctx:LangParser.BodyContext):
        global tab
        tab += 1
        body = []
        children = ctx.getChildren()
        for child in children:
            if isinstance(child, LangParser.LineContext):
                body.append("\t"*tab+str(self.enterLine(child))+"\n")
        tab -= 1
        return ''.join(body)

    def exitBody(self, ctx:LangParser.BodyContext):
        pass



# ---------------------  CODE
    def enterCode(self, ctx:LangParser.CodeContext):
        global tab
        tab = 1
        child = ctx.getChild(0)
        if isinstance(child, LangParser.Fun_defContext) :
            print('\n', '\t'*tab, end='')   #robi TAB przed atrybutami klasy i definicjami funkcji klasy
        if isinstance(child,LangParser.DefinitionContext):
            print('\n', '\t' * tab, end='')
            df = self.enterDefinition(child)
          #  pf.write(df)
            print(df)

    def exitCode(self, ctx:LangParser.CodeContext):
        global tab
        tab -= 1

    def enterMain(self, ctx:LangParser.MainContext):
        print('def main(): ')
        body = self.enterBody(ctx.getChild(1))
        print(body)

    def exitMain(self, ctx:LangParser.MainContext):
        pass



def main():

    orig_stdout = sys.stdout
    #setting up a file where program will translate code to Python
    f = open('python_file.py', 'w')
    sys.stdout = f


    input_stream = FileStream("test1.txt")  # sys.argv[1])
    lexer = LangLexer(input_stream)
    # lexer = LangLexer(StdinStream())
    tokens = CommonTokenStream(lexer)
    parser = LangParser(tokens)

    tree = parser.class_def()
    listener = LangVarListener()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)


   #adding string to file works

    sys.stdout = orig_stdout
    f.close()



if __name__ == '__main__':
    main()
