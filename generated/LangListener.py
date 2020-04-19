# Generated from Lang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#var_type.
    def enterVar_type(self, ctx:LangParser.Var_typeContext):
        pass

    # Exit a parse tree produced by LangParser#var_type.
    def exitVar_type(self, ctx:LangParser.Var_typeContext):
        pass


    # Enter a parse tree produced by LangParser#operator.
    def enterOperator(self, ctx:LangParser.OperatorContext):
        pass

    # Exit a parse tree produced by LangParser#operator.
    def exitOperator(self, ctx:LangParser.OperatorContext):
        pass


    # Enter a parse tree produced by LangParser#logical_operator.
    def enterLogical_operator(self, ctx:LangParser.Logical_operatorContext):
        pass

    # Exit a parse tree produced by LangParser#logical_operator.
    def exitLogical_operator(self, ctx:LangParser.Logical_operatorContext):
        pass


    # Enter a parse tree produced by LangParser#relation_operator.
    def enterRelation_operator(self, ctx:LangParser.Relation_operatorContext):
        pass

    # Exit a parse tree produced by LangParser#relation_operator.
    def exitRelation_operator(self, ctx:LangParser.Relation_operatorContext):
        pass


    # Enter a parse tree produced by LangParser#declaration.
    def enterDeclaration(self, ctx:LangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by LangParser#declaration.
    def exitDeclaration(self, ctx:LangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by LangParser#definition.
    def enterDefinition(self, ctx:LangParser.DefinitionContext):
        pass

    # Exit a parse tree produced by LangParser#definition.
    def exitDefinition(self, ctx:LangParser.DefinitionContext):
        pass


    # Enter a parse tree produced by LangParser#assign_val.
    def enterAssign_val(self, ctx:LangParser.Assign_valContext):
        pass

    # Exit a parse tree produced by LangParser#assign_val.
    def exitAssign_val(self, ctx:LangParser.Assign_valContext):
        pass


    # Enter a parse tree produced by LangParser#assignment.
    def enterAssignment(self, ctx:LangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LangParser#assignment.
    def exitAssignment(self, ctx:LangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LangParser#value.
    def enterValue(self, ctx:LangParser.ValueContext):
        pass

    # Exit a parse tree produced by LangParser#value.
    def exitValue(self, ctx:LangParser.ValueContext):
        pass


    # Enter a parse tree produced by LangParser#var_or_num_value.
    def enterVar_or_num_value(self, ctx:LangParser.Var_or_num_valueContext):
        pass

    # Exit a parse tree produced by LangParser#var_or_num_value.
    def exitVar_or_num_value(self, ctx:LangParser.Var_or_num_valueContext):
        pass


    # Enter a parse tree produced by LangParser#math_operation.
    def enterMath_operation(self, ctx:LangParser.Math_operationContext):
        pass

    # Exit a parse tree produced by LangParser#math_operation.
    def exitMath_operation(self, ctx:LangParser.Math_operationContext):
        pass


    # Enter a parse tree produced by LangParser#fun_call.
    def enterFun_call(self, ctx:LangParser.Fun_callContext):
        pass

    # Exit a parse tree produced by LangParser#fun_call.
    def exitFun_call(self, ctx:LangParser.Fun_callContext):
        pass


    # Enter a parse tree produced by LangParser#fun_args.
    def enterFun_args(self, ctx:LangParser.Fun_argsContext):
        pass

    # Exit a parse tree produced by LangParser#fun_args.
    def exitFun_args(self, ctx:LangParser.Fun_argsContext):
        pass


    # Enter a parse tree produced by LangParser#fun_params.
    def enterFun_params(self, ctx:LangParser.Fun_paramsContext):
        pass

    # Exit a parse tree produced by LangParser#fun_params.
    def exitFun_params(self, ctx:LangParser.Fun_paramsContext):
        pass


    # Enter a parse tree produced by LangParser#fun_declaration.
    def enterFun_declaration(self, ctx:LangParser.Fun_declarationContext):
        pass

    # Exit a parse tree produced by LangParser#fun_declaration.
    def exitFun_declaration(self, ctx:LangParser.Fun_declarationContext):
        pass


    # Enter a parse tree produced by LangParser#fun_def.
    def enterFun_def(self, ctx:LangParser.Fun_defContext):
        pass

    # Exit a parse tree produced by LangParser#fun_def.
    def exitFun_def(self, ctx:LangParser.Fun_defContext):
        pass


    # Enter a parse tree produced by LangParser#class_def.
    def enterClass_def(self, ctx:LangParser.Class_defContext):
        pass

    # Exit a parse tree produced by LangParser#class_def.
    def exitClass_def(self, ctx:LangParser.Class_defContext):
        pass


    # Enter a parse tree produced by LangParser#printf.
    def enterPrintf(self, ctx:LangParser.PrintfContext):
        pass

    # Exit a parse tree produced by LangParser#printf.
    def exitPrintf(self, ctx:LangParser.PrintfContext):
        pass


    # Enter a parse tree produced by LangParser#return_value.
    def enterReturn_value(self, ctx:LangParser.Return_valueContext):
        pass

    # Exit a parse tree produced by LangParser#return_value.
    def exitReturn_value(self, ctx:LangParser.Return_valueContext):
        pass


    # Enter a parse tree produced by LangParser#line.
    def enterLine(self, ctx:LangParser.LineContext):
        pass

    # Exit a parse tree produced by LangParser#line.
    def exitLine(self, ctx:LangParser.LineContext):
        pass


    # Enter a parse tree produced by LangParser#line_semi.
    def enterLine_semi(self, ctx:LangParser.Line_semiContext):
        pass

    # Exit a parse tree produced by LangParser#line_semi.
    def exitLine_semi(self, ctx:LangParser.Line_semiContext):
        pass


    # Enter a parse tree produced by LangParser#body.
    def enterBody(self, ctx:LangParser.BodyContext):
        pass

    # Exit a parse tree produced by LangParser#body.
    def exitBody(self, ctx:LangParser.BodyContext):
        pass


    # Enter a parse tree produced by LangParser#code.
    def enterCode(self, ctx:LangParser.CodeContext):
        pass

    # Exit a parse tree produced by LangParser#code.
    def exitCode(self, ctx:LangParser.CodeContext):
        pass


    # Enter a parse tree produced by LangParser#main.
    def enterMain(self, ctx:LangParser.MainContext):
        pass

    # Exit a parse tree produced by LangParser#main.
    def exitMain(self, ctx:LangParser.MainContext):
        pass


    # Enter a parse tree produced by LangParser#conditions.
    def enterConditions(self, ctx:LangParser.ConditionsContext):
        pass

    # Exit a parse tree produced by LangParser#conditions.
    def exitConditions(self, ctx:LangParser.ConditionsContext):
        pass


    # Enter a parse tree produced by LangParser#condition.
    def enterCondition(self, ctx:LangParser.ConditionContext):
        pass

    # Exit a parse tree produced by LangParser#condition.
    def exitCondition(self, ctx:LangParser.ConditionContext):
        pass


    # Enter a parse tree produced by LangParser#logical_stmt.
    def enterLogical_stmt(self, ctx:LangParser.Logical_stmtContext):
        pass

    # Exit a parse tree produced by LangParser#logical_stmt.
    def exitLogical_stmt(self, ctx:LangParser.Logical_stmtContext):
        pass


    # Enter a parse tree produced by LangParser#brack_logical_stm.
    def enterBrack_logical_stm(self, ctx:LangParser.Brack_logical_stmContext):
        pass

    # Exit a parse tree produced by LangParser#brack_logical_stm.
    def exitBrack_logical_stm(self, ctx:LangParser.Brack_logical_stmContext):
        pass


    # Enter a parse tree produced by LangParser#if_def.
    def enterIf_def(self, ctx:LangParser.If_defContext):
        pass

    # Exit a parse tree produced by LangParser#if_def.
    def exitIf_def(self, ctx:LangParser.If_defContext):
        pass


    # Enter a parse tree produced by LangParser#for_def.
    def enterFor_def(self, ctx:LangParser.For_defContext):
        pass

    # Exit a parse tree produced by LangParser#for_def.
    def exitFor_def(self, ctx:LangParser.For_defContext):
        pass


    # Enter a parse tree produced by LangParser#while_def.
    def enterWhile_def(self, ctx:LangParser.While_defContext):
        pass

    # Exit a parse tree produced by LangParser#while_def.
    def exitWhile_def(self, ctx:LangParser.While_defContext):
        pass


    # Enter a parse tree produced by LangParser#increment.
    def enterIncrement(self, ctx:LangParser.IncrementContext):
        pass

    # Exit a parse tree produced by LangParser#increment.
    def exitIncrement(self, ctx:LangParser.IncrementContext):
        pass


    # Enter a parse tree produced by LangParser#decrement.
    def enterDecrement(self, ctx:LangParser.DecrementContext):
        pass

    # Exit a parse tree produced by LangParser#decrement.
    def exitDecrement(self, ctx:LangParser.DecrementContext):
        pass


