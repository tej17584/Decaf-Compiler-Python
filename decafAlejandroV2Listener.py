# Generated from decafAlejandroV2.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .decafAlejandroV2Parser import decafAlejandroV2Parser
else:
    from decafAlejandroV2Parser import decafAlejandroV2Parser

# This class defines a complete listener for a parse tree produced by decafAlejandroV2Parser.
class decafAlejandroV2Listener(ParseTreeListener):

    # Enter a parse tree produced by decafAlejandroV2Parser#program.
    def enterProgram(self, ctx:decafAlejandroV2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#program.
    def exitProgram(self, ctx:decafAlejandroV2Parser.ProgramContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#declaration.
    def enterDeclaration(self, ctx:decafAlejandroV2Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#declaration.
    def exitDeclaration(self, ctx:decafAlejandroV2Parser.DeclarationContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#vardeclr.
    def enterVardeclr(self, ctx:decafAlejandroV2Parser.VardeclrContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#vardeclr.
    def exitVardeclr(self, ctx:decafAlejandroV2Parser.VardeclrContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#field_declr.
    def enterField_declr(self, ctx:decafAlejandroV2Parser.Field_declrContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#field_declr.
    def exitField_declr(self, ctx:decafAlejandroV2Parser.Field_declrContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#array_id.
    def enterArray_id(self, ctx:decafAlejandroV2Parser.Array_idContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#array_id.
    def exitArray_id(self, ctx:decafAlejandroV2Parser.Array_idContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#field_var.
    def enterField_var(self, ctx:decafAlejandroV2Parser.Field_varContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#field_var.
    def exitField_var(self, ctx:decafAlejandroV2Parser.Field_varContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#var_id.
    def enterVar_id(self, ctx:decafAlejandroV2Parser.Var_idContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#var_id.
    def exitVar_id(self, ctx:decafAlejandroV2Parser.Var_idContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#struct_declr.
    def enterStruct_declr(self, ctx:decafAlejandroV2Parser.Struct_declrContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#struct_declr.
    def exitStruct_declr(self, ctx:decafAlejandroV2Parser.Struct_declrContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#method_declr.
    def enterMethod_declr(self, ctx:decafAlejandroV2Parser.Method_declrContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#method_declr.
    def exitMethod_declr(self, ctx:decafAlejandroV2Parser.Method_declrContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#return_type.
    def enterReturn_type(self, ctx:decafAlejandroV2Parser.Return_typeContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#return_type.
    def exitReturn_type(self, ctx:decafAlejandroV2Parser.Return_typeContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#block.
    def enterBlock(self, ctx:decafAlejandroV2Parser.BlockContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#block.
    def exitBlock(self, ctx:decafAlejandroV2Parser.BlockContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#statement_assign.
    def enterStatement_assign(self, ctx:decafAlejandroV2Parser.Statement_assignContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#statement_assign.
    def exitStatement_assign(self, ctx:decafAlejandroV2Parser.Statement_assignContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#statement_methodcall.
    def enterStatement_methodcall(self, ctx:decafAlejandroV2Parser.Statement_methodcallContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#statement_methodcall.
    def exitStatement_methodcall(self, ctx:decafAlejandroV2Parser.Statement_methodcallContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#statement_if.
    def enterStatement_if(self, ctx:decafAlejandroV2Parser.Statement_ifContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#statement_if.
    def exitStatement_if(self, ctx:decafAlejandroV2Parser.Statement_ifContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#statement_while.
    def enterStatement_while(self, ctx:decafAlejandroV2Parser.Statement_whileContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#statement_while.
    def exitStatement_while(self, ctx:decafAlejandroV2Parser.Statement_whileContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#statement_return.
    def enterStatement_return(self, ctx:decafAlejandroV2Parser.Statement_returnContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#statement_return.
    def exitStatement_return(self, ctx:decafAlejandroV2Parser.Statement_returnContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#statement_for.
    def enterStatement_for(self, ctx:decafAlejandroV2Parser.Statement_forContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#statement_for.
    def exitStatement_for(self, ctx:decafAlejandroV2Parser.Statement_forContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#statement_break.
    def enterStatement_break(self, ctx:decafAlejandroV2Parser.Statement_breakContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#statement_break.
    def exitStatement_break(self, ctx:decafAlejandroV2Parser.Statement_breakContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#method_call.
    def enterMethod_call(self, ctx:decafAlejandroV2Parser.Method_callContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#method_call.
    def exitMethod_call(self, ctx:decafAlejandroV2Parser.Method_callContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#expr_literal.
    def enterExpr_literal(self, ctx:decafAlejandroV2Parser.Expr_literalContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#expr_literal.
    def exitExpr_literal(self, ctx:decafAlejandroV2Parser.Expr_literalContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#expr_location.
    def enterExpr_location(self, ctx:decafAlejandroV2Parser.Expr_locationContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#expr_location.
    def exitExpr_location(self, ctx:decafAlejandroV2Parser.Expr_locationContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#expr_PrecedenciaMax.
    def enterExpr_PrecedenciaMax(self, ctx:decafAlejandroV2Parser.Expr_PrecedenciaMaxContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#expr_PrecedenciaMax.
    def exitExpr_PrecedenciaMax(self, ctx:decafAlejandroV2Parser.Expr_PrecedenciaMaxContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#expr_menos.
    def enterExpr_menos(self, ctx:decafAlejandroV2Parser.Expr_menosContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#expr_menos.
    def exitExpr_menos(self, ctx:decafAlejandroV2Parser.Expr_menosContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#expr_normal.
    def enterExpr_normal(self, ctx:decafAlejandroV2Parser.Expr_normalContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#expr_normal.
    def exitExpr_normal(self, ctx:decafAlejandroV2Parser.Expr_normalContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#expr_PrecedenciaMenor.
    def enterExpr_PrecedenciaMenor(self, ctx:decafAlejandroV2Parser.Expr_PrecedenciaMenorContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#expr_PrecedenciaMenor.
    def exitExpr_PrecedenciaMenor(self, ctx:decafAlejandroV2Parser.Expr_PrecedenciaMenorContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#expr_parentesis.
    def enterExpr_parentesis(self, ctx:decafAlejandroV2Parser.Expr_parentesisContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#expr_parentesis.
    def exitExpr_parentesis(self, ctx:decafAlejandroV2Parser.Expr_parentesisContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#expr_methodCall.
    def enterExpr_methodCall(self, ctx:decafAlejandroV2Parser.Expr_methodCallContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#expr_methodCall.
    def exitExpr_methodCall(self, ctx:decafAlejandroV2Parser.Expr_methodCallContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#expr_negacion.
    def enterExpr_negacion(self, ctx:decafAlejandroV2Parser.Expr_negacionContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#expr_negacion.
    def exitExpr_negacion(self, ctx:decafAlejandroV2Parser.Expr_negacionContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#location.
    def enterLocation(self, ctx:decafAlejandroV2Parser.LocationContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#location.
    def exitLocation(self, ctx:decafAlejandroV2Parser.LocationContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#int_literal.
    def enterInt_literal(self, ctx:decafAlejandroV2Parser.Int_literalContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#int_literal.
    def exitInt_literal(self, ctx:decafAlejandroV2Parser.Int_literalContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#string_literal.
    def enterString_literal(self, ctx:decafAlejandroV2Parser.String_literalContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#string_literal.
    def exitString_literal(self, ctx:decafAlejandroV2Parser.String_literalContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#bool_literal.
    def enterBool_literal(self, ctx:decafAlejandroV2Parser.Bool_literalContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#bool_literal.
    def exitBool_literal(self, ctx:decafAlejandroV2Parser.Bool_literalContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#rel_op.
    def enterRel_op(self, ctx:decafAlejandroV2Parser.Rel_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#rel_op.
    def exitRel_op(self, ctx:decafAlejandroV2Parser.Rel_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#eq_op.
    def enterEq_op(self, ctx:decafAlejandroV2Parser.Eq_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#eq_op.
    def exitEq_op(self, ctx:decafAlejandroV2Parser.Eq_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#cond_op.
    def enterCond_op(self, ctx:decafAlejandroV2Parser.Cond_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#cond_op.
    def exitCond_op(self, ctx:decafAlejandroV2Parser.Cond_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#literal.
    def enterLiteral(self, ctx:decafAlejandroV2Parser.LiteralContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#literal.
    def exitLiteral(self, ctx:decafAlejandroV2Parser.LiteralContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#arith_op.
    def enterArith_op(self, ctx:decafAlejandroV2Parser.Arith_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#arith_op.
    def exitArith_op(self, ctx:decafAlejandroV2Parser.Arith_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#var_type.
    def enterVar_type(self, ctx:decafAlejandroV2Parser.Var_typeContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#var_type.
    def exitVar_type(self, ctx:decafAlejandroV2Parser.Var_typeContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#assign_op.
    def enterAssign_op(self, ctx:decafAlejandroV2Parser.Assign_opContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#assign_op.
    def exitAssign_op(self, ctx:decafAlejandroV2Parser.Assign_opContext):
        pass


    # Enter a parse tree produced by decafAlejandroV2Parser#method_name.
    def enterMethod_name(self, ctx:decafAlejandroV2Parser.Method_nameContext):
        pass

    # Exit a parse tree produced by decafAlejandroV2Parser#method_name.
    def exitMethod_name(self, ctx:decafAlejandroV2Parser.Method_nameContext):
        pass



del decafAlejandroV2Parser