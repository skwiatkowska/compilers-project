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

    def enterRelation_operator(self, ctx: LangParser.Relation_operatorContext):
        if ctx.NOT_EQUAL():
            print(" != ", end='')
        elif ctx.EQUAL():
            print(" == ", end='')
        elif ctx.GREATER_EQ():
            print(" >= ", end='')
        elif ctx.GREATER():
            print(" > ", end='')
        elif ctx.LESS():
            print(" < ", end='')
        elif ctx.LESS_EQ():
            print(" <= ", end='')


    # def enterDeclaration(self, ctx: LangParser.Class_defContext):
    #    print(ctx.NAME().getText())

    def enterDefinition(self, ctx: LangParser.DefinitionContext):
        child = ctx.getChild(0)
        print(child.NAME().getText(), "= ", end='')

    def exitDefinition(self, ctx: LangParser.DefinitionContext):
        print("")

    def enterAssign_val(self, ctx: LangParser.Assign_valContext):
        # child = ctx.getChild(0)
        # print(child.NAME().getText(), end='')
        pass  # print("=", ctx.NAME().getText())

    def enterAssignment(self, ctx: LangParser.AssignmentContext):
        print(ctx.NAME().getText(), "= ", end='')

    def exitAssignment(self, ctx: LangParser.AssignmentContext):
        print()

    def enterValue(self, ctx: LangParser.ValueContext):
        if ctx.STRING_VAL():
            print(ctx.STRING_VAL().getText(), end='')

    def enterVar_or_num_value(self, ctx: LangParser.Var_or_num_valueContext):
        if ctx.NAME():
            print(ctx.NAME().getText(), end='')
        elif ctx.INT_VAL:
            print(ctx.INT_VAL().getText(), end='')
        elif ctx.INT_VAL:
            print(ctx.DOUBLE_VAL().getText(), end='')
			
			
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
        print("\nreturn ", end='')

    def exitReturn_value(self, ctx: LangParser.Return_valueContext):
        print()

	def enterIncrement(self, ctx: LangParser.IncrementContext):
        print(ctx.NAME().getText(), "+= 1")

    def enterDecrement(self, ctx: LangParser.DecrementContext):
        print(ctx.NAME().getText(), "-= 1")

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
