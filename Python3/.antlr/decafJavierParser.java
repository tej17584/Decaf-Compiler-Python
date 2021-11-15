// Generated from c:\Users\josea\Desktop\Compiladores\compis_Proyecto1\Python3\decafJavier.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class decafJavierParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, PROGRAM=2, IF=3, ELSE=4, FOR=5, RETURN=6, BREAK=7, CONTINUE=8, 
		BOOLEAN=9, CHAR=10, INT=11, STRING=12, TRUE=13, FALSE=14, VOID=15, CALLOUT=16, 
		SEMICOLON=17, LCURLY=18, RCURLY=19, LSQUARE=20, RSQUARE=21, LROUND=22, 
		RROUND=23, COMMA=24, QUOTES=25, APOSTROPHE=26, ADD=27, SUB=28, MULTIPLY=29, 
		DIVIDE=30, REMINDER=31, AND=32, OR=33, NOT=34, GREATER_OP=35, LESS_OP=36, 
		GREATER_eq_op=37, LESS_eq_op=38, EQUAL_OP=39, ADD_eq_op=40, SUB_eq_op=41, 
		EQUALITY_OP=42, UNEQUALITY_OP=43, ID=44, ALPHA=45, CHAR_LITERAL=46, DECIMAL_LITERAL=47, 
		DIGIT=48, HEX_LITERAL=49, BOOL_LITERAL=50, STRING_LITERAL=51, ALPHA_NUM=52, 
		HEX_DIGIT=53, LINE_COMMENT=54, COMMENT=55, NEWLINE=56, WHITESPACE=57;
	public static final int
		RULE_program = 0, RULE_vardeclr = 1, RULE_field_declr = 2, RULE_array_id = 3, 
		RULE_field_var = 4, RULE_var_id = 5, RULE_method_declr = 6, RULE_return_type = 7, 
		RULE_block = 8, RULE_statement = 9, RULE_method_call_inter = 10, RULE_method_call = 11, 
		RULE_expr = 12, RULE_location = 13, RULE_callout_arg = 14, RULE_int_literal = 15, 
		RULE_rel_op = 16, RULE_eq_op = 17, RULE_cond_op = 18, RULE_literal = 19, 
		RULE_bin_op = 20, RULE_arith_op = 21, RULE_var_type = 22, RULE_assign_op = 23, 
		RULE_method_name = 24;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "vardeclr", "field_declr", "array_id", "field_var", "var_id", 
			"method_declr", "return_type", "block", "statement", "method_call_inter", 
			"method_call", "expr", "location", "callout_arg", "int_literal", "rel_op", 
			"eq_op", "cond_op", "literal", "bin_op", "arith_op", "var_type", "assign_op", 
			"method_name"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'Program'", "'if'", "'else'", "'for'", "'return'", 
			"'break'", "'continue'", "'boolean'", "'char'", "'int'", "'string'", 
			"'True'", "'False'", "'void'", "'callout'", "';'", "'{'", "'}'", "'['", 
			"']'", "'('", "')'", "','", "'\"'", "'''", "'+'", "'-'", "'*'", "'/'", 
			"'%'", "'&&'", "'||'", "'!'", "'>'", "'<'", "'>='", "'<='", "'='", "'+='", 
			"'-='", "'=='", "'!='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "PROGRAM", "IF", "ELSE", "FOR", "RETURN", "BREAK", "CONTINUE", 
			"BOOLEAN", "CHAR", "INT", "STRING", "TRUE", "FALSE", "VOID", "CALLOUT", 
			"SEMICOLON", "LCURLY", "RCURLY", "LSQUARE", "RSQUARE", "LROUND", "RROUND", 
			"COMMA", "QUOTES", "APOSTROPHE", "ADD", "SUB", "MULTIPLY", "DIVIDE", 
			"REMINDER", "AND", "OR", "NOT", "GREATER_OP", "LESS_OP", "GREATER_eq_op", 
			"LESS_eq_op", "EQUAL_OP", "ADD_eq_op", "SUB_eq_op", "EQUALITY_OP", "UNEQUALITY_OP", 
			"ID", "ALPHA", "CHAR_LITERAL", "DECIMAL_LITERAL", "DIGIT", "HEX_LITERAL", 
			"BOOL_LITERAL", "STRING_LITERAL", "ALPHA_NUM", "HEX_DIGIT", "LINE_COMMENT", 
			"COMMENT", "NEWLINE", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "decafJavier.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public decafJavierParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(decafJavierParser.CLASS, 0); }
		public TerminalNode PROGRAM() { return getToken(decafJavierParser.PROGRAM, 0); }
		public TerminalNode LCURLY() { return getToken(decafJavierParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(decafJavierParser.RCURLY, 0); }
		public List<Field_declrContext> field_declr() {
			return getRuleContexts(Field_declrContext.class);
		}
		public Field_declrContext field_declr(int i) {
			return getRuleContext(Field_declrContext.class,i);
		}
		public List<Method_declrContext> method_declr() {
			return getRuleContexts(Method_declrContext.class);
		}
		public Method_declrContext method_declr(int i) {
			return getRuleContext(Method_declrContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(CLASS);
			setState(51);
			match(PROGRAM);
			setState(52);
			match(LCURLY);
			setState(56);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(53);
					field_declr();
					}
					} 
				}
				setState(58);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << INT) | (1L << VOID))) != 0)) {
				{
				{
				setState(59);
				method_declr();
				}
				}
				setState(64);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(65);
			match(RCURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardeclrContext extends ParserRuleContext {
		public TerminalNode SEMICOLON() { return getToken(decafJavierParser.SEMICOLON, 0); }
		public List<Var_typeContext> var_type() {
			return getRuleContexts(Var_typeContext.class);
		}
		public Var_typeContext var_type(int i) {
			return getRuleContext(Var_typeContext.class,i);
		}
		public List<Field_varContext> field_var() {
			return getRuleContexts(Field_varContext.class);
		}
		public Field_varContext field_var(int i) {
			return getRuleContext(Field_varContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(decafJavierParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(decafJavierParser.COMMA, i);
		}
		public VardeclrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardeclr; }
	}

	public final VardeclrContext vardeclr() throws RecognitionException {
		VardeclrContext _localctx = new VardeclrContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_vardeclr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(67);
			var_type();
			setState(68);
			field_var();
			}
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(70);
				match(COMMA);
				setState(71);
				var_type();
				setState(72);
				field_var();
				}
				}
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(79);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Field_declrContext extends ParserRuleContext {
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public List<Field_varContext> field_var() {
			return getRuleContexts(Field_varContext.class);
		}
		public Field_varContext field_var(int i) {
			return getRuleContext(Field_varContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(decafJavierParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(decafJavierParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(decafJavierParser.COMMA, i);
		}
		public Field_declrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_declr; }
	}

	public final Field_declrContext field_declr() throws RecognitionException {
		Field_declrContext _localctx = new Field_declrContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_field_declr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			var_type();
			setState(82);
			field_var();
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(83);
				match(COMMA);
				setState(84);
				field_var();
				}
				}
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(90);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_idContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(decafJavierParser.ID, 0); }
		public TerminalNode LSQUARE() { return getToken(decafJavierParser.LSQUARE, 0); }
		public Int_literalContext int_literal() {
			return getRuleContext(Int_literalContext.class,0);
		}
		public TerminalNode RSQUARE() { return getToken(decafJavierParser.RSQUARE, 0); }
		public Array_idContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_id; }
	}

	public final Array_idContext array_id() throws RecognitionException {
		Array_idContext _localctx = new Array_idContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_array_id);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(ID);
			setState(93);
			match(LSQUARE);
			setState(94);
			int_literal();
			setState(95);
			match(RSQUARE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Field_varContext extends ParserRuleContext {
		public Var_idContext var_id() {
			return getRuleContext(Var_idContext.class,0);
		}
		public Array_idContext array_id() {
			return getRuleContext(Array_idContext.class,0);
		}
		public Field_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_var; }
	}

	public final Field_varContext field_var() throws RecognitionException {
		Field_varContext _localctx = new Field_varContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_field_var);
		try {
			setState(99);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(97);
				var_id();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(98);
				array_id();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_idContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(decafJavierParser.ID, 0); }
		public Var_idContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_id; }
	}

	public final Var_idContext var_id() throws RecognitionException {
		Var_idContext _localctx = new Var_idContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_var_id);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_declrContext extends ParserRuleContext {
		public Return_typeContext return_type() {
			return getRuleContext(Return_typeContext.class,0);
		}
		public Method_nameContext method_name() {
			return getRuleContext(Method_nameContext.class,0);
		}
		public TerminalNode LROUND() { return getToken(decafJavierParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(decafJavierParser.RROUND, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<Var_typeContext> var_type() {
			return getRuleContexts(Var_typeContext.class);
		}
		public Var_typeContext var_type(int i) {
			return getRuleContext(Var_typeContext.class,i);
		}
		public List<Var_idContext> var_id() {
			return getRuleContexts(Var_idContext.class);
		}
		public Var_idContext var_id(int i) {
			return getRuleContext(Var_idContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(decafJavierParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(decafJavierParser.COMMA, i);
		}
		public Method_declrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_declr; }
	}

	public final Method_declrContext method_declr() throws RecognitionException {
		Method_declrContext _localctx = new Method_declrContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_method_declr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			return_type();
			setState(104);
			method_name();
			setState(105);
			match(LROUND);
			setState(118);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BOOLEAN || _la==INT) {
				{
				{
				setState(106);
				var_type();
				setState(107);
				var_id();
				}
				setState(115);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(109);
					match(COMMA);
					setState(110);
					var_type();
					setState(111);
					var_id();
					}
					}
					setState(117);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(120);
			match(RROUND);
			setState(121);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_typeContext extends ParserRuleContext {
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public TerminalNode VOID() { return getToken(decafJavierParser.VOID, 0); }
		public Return_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_type; }
	}

	public final Return_typeContext return_type() throws RecognitionException {
		Return_typeContext _localctx = new Return_typeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_return_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLEAN:
			case INT:
				{
				setState(123);
				var_type();
				}
				break;
			case VOID:
				{
				setState(124);
				match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LCURLY() { return getToken(decafJavierParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(decafJavierParser.RCURLY, 0); }
		public List<VardeclrContext> vardeclr() {
			return getRuleContexts(VardeclrContext.class);
		}
		public VardeclrContext vardeclr(int i) {
			return getRuleContext(VardeclrContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(LCURLY);
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BOOLEAN || _la==INT) {
				{
				{
				setState(128);
				vardeclr();
				}
				}
				setState(133);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << FOR) | (1L << RETURN) | (1L << BREAK) | (1L << CALLOUT) | (1L << ID))) != 0)) {
				{
				{
				setState(134);
				statement();
				}
				}
				setState(139);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(140);
			match(RCURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public Assign_opContext assign_op() {
			return getRuleContext(Assign_opContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(decafJavierParser.SEMICOLON, 0); }
		public Method_callContext method_call() {
			return getRuleContext(Method_callContext.class,0);
		}
		public TerminalNode IF() { return getToken(decafJavierParser.IF, 0); }
		public TerminalNode LROUND() { return getToken(decafJavierParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(decafJavierParser.RROUND, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(decafJavierParser.ELSE, 0); }
		public List<Var_idContext> var_id() {
			return getRuleContexts(Var_idContext.class);
		}
		public Var_idContext var_id(int i) {
			return getRuleContext(Var_idContext.class,i);
		}
		public List<TerminalNode> EQUAL_OP() { return getTokens(decafJavierParser.EQUAL_OP); }
		public TerminalNode EQUAL_OP(int i) {
			return getToken(decafJavierParser.EQUAL_OP, i);
		}
		public TerminalNode RETURN() { return getToken(decafJavierParser.RETURN, 0); }
		public TerminalNode FOR() { return getToken(decafJavierParser.FOR, 0); }
		public TerminalNode COMMA() { return getToken(decafJavierParser.COMMA, 0); }
		public List<Int_literalContext> int_literal() {
			return getRuleContexts(Int_literalContext.class);
		}
		public Int_literalContext int_literal(int i) {
			return getRuleContext(Int_literalContext.class,i);
		}
		public TerminalNode BREAK() { return getToken(decafJavierParser.BREAK, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_statement);
		int _la;
		try {
			setState(189);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(142);
				location();
				setState(143);
				assign_op();
				setState(144);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(146);
				location();
				setState(147);
				assign_op();
				setState(148);
				expr(0);
				setState(149);
				match(SEMICOLON);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(151);
				method_call();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(152);
				match(IF);
				setState(153);
				match(LROUND);
				setState(154);
				expr(0);
				setState(155);
				match(RROUND);
				setState(156);
				block();
				setState(159);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ELSE) {
					{
					setState(157);
					match(ELSE);
					setState(158);
					block();
					}
				}

				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(161);
				var_id();
				setState(162);
				match(EQUAL_OP);
				setState(163);
				expr(0);
				setState(164);
				match(SEMICOLON);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(166);
				match(RETURN);
				setState(167);
				expr(0);
				setState(168);
				match(SEMICOLON);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(170);
				match(FOR);
				setState(171);
				var_id();
				setState(174);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==EQUAL_OP) {
					{
					setState(172);
					match(EQUAL_OP);
					setState(173);
					int_literal();
					}
				}

				setState(176);
				match(COMMA);
				setState(183);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					{
					setState(177);
					var_id();
					setState(180);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==EQUAL_OP) {
						{
						setState(178);
						match(EQUAL_OP);
						setState(179);
						int_literal();
						}
					}

					}
					}
					break;
				case DECIMAL_LITERAL:
				case HEX_LITERAL:
					{
					setState(182);
					int_literal();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(185);
				block();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(187);
				match(BREAK);
				setState(188);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_call_interContext extends ParserRuleContext {
		public Method_nameContext method_name() {
			return getRuleContext(Method_nameContext.class,0);
		}
		public TerminalNode LROUND() { return getToken(decafJavierParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(decafJavierParser.RROUND, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(decafJavierParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(decafJavierParser.COMMA, i);
		}
		public Method_call_interContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_call_inter; }
	}

	public final Method_call_interContext method_call_inter() throws RecognitionException {
		Method_call_interContext _localctx = new Method_call_interContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_method_call_inter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			method_name();
			setState(192);
			match(LROUND);
			setState(201);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CALLOUT) | (1L << LROUND) | (1L << SUB) | (1L << NOT) | (1L << ID) | (1L << CHAR_LITERAL) | (1L << DECIMAL_LITERAL) | (1L << HEX_LITERAL) | (1L << BOOL_LITERAL))) != 0)) {
				{
				setState(193);
				expr(0);
				setState(198);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(194);
					match(COMMA);
					setState(195);
					expr(0);
					}
					}
					setState(200);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(203);
			match(RROUND);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_callContext extends ParserRuleContext {
		public Method_call_interContext method_call_inter() {
			return getRuleContext(Method_call_interContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(decafJavierParser.SEMICOLON, 0); }
		public TerminalNode CALLOUT() { return getToken(decafJavierParser.CALLOUT, 0); }
		public TerminalNode LROUND() { return getToken(decafJavierParser.LROUND, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(decafJavierParser.STRING_LITERAL, 0); }
		public TerminalNode RROUND() { return getToken(decafJavierParser.RROUND, 0); }
		public List<TerminalNode> COMMA() { return getTokens(decafJavierParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(decafJavierParser.COMMA, i);
		}
		public List<Callout_argContext> callout_arg() {
			return getRuleContexts(Callout_argContext.class);
		}
		public Callout_argContext callout_arg(int i) {
			return getRuleContext(Callout_argContext.class,i);
		}
		public Method_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_call; }
	}

	public final Method_callContext method_call() throws RecognitionException {
		Method_callContext _localctx = new Method_callContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_method_call);
		int _la;
		try {
			setState(225);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				method_call_inter();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				method_call_inter();
				setState(207);
				match(SEMICOLON);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(209);
				match(CALLOUT);
				setState(210);
				match(LROUND);
				setState(211);
				match(STRING_LITERAL);
				setState(221);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(212);
					match(COMMA);
					setState(213);
					callout_arg();
					setState(218);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(214);
						match(COMMA);
						setState(215);
						callout_arg();
						}
						}
						setState(220);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(223);
				match(RROUND);
				setState(224);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode SUB() { return getToken(decafJavierParser.SUB, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public Method_callContext method_call() {
			return getRuleContext(Method_callContext.class,0);
		}
		public TerminalNode NOT() { return getToken(decafJavierParser.NOT, 0); }
		public TerminalNode LROUND() { return getToken(decafJavierParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(decafJavierParser.RROUND, 0); }
		public Bin_opContext bin_op() {
			return getRuleContext(Bin_opContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(228);
				location();
				}
				break;
			case 2:
				{
				setState(229);
				literal();
				}
				break;
			case 3:
				{
				setState(230);
				match(SUB);
				setState(231);
				expr(4);
				}
				break;
			case 4:
				{
				setState(232);
				method_call();
				}
				break;
			case 5:
				{
				setState(233);
				match(NOT);
				setState(234);
				expr(2);
				}
				break;
			case 6:
				{
				setState(235);
				match(LROUND);
				setState(236);
				expr(0);
				setState(237);
				match(RROUND);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(247);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(241);
					if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
					setState(242);
					bin_op();
					setState(243);
					expr(6);
					}
					} 
				}
				setState(249);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class LocationContext extends ParserRuleContext {
		public Var_idContext var_id() {
			return getRuleContext(Var_idContext.class,0);
		}
		public Array_idContext array_id() {
			return getRuleContext(Array_idContext.class,0);
		}
		public LocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_location; }
	}

	public final LocationContext location() throws RecognitionException {
		LocationContext _localctx = new LocationContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_location);
		try {
			setState(252);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(250);
				var_id();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(251);
				array_id();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Callout_argContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode STRING_LITERAL() { return getToken(decafJavierParser.STRING_LITERAL, 0); }
		public Callout_argContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callout_arg; }
	}

	public final Callout_argContext callout_arg() throws RecognitionException {
		Callout_argContext _localctx = new Callout_argContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_callout_arg);
		try {
			setState(256);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CALLOUT:
			case LROUND:
			case SUB:
			case NOT:
			case ID:
			case CHAR_LITERAL:
			case DECIMAL_LITERAL:
			case HEX_LITERAL:
			case BOOL_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(254);
				expr(0);
				}
				break;
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(255);
				match(STRING_LITERAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Int_literalContext extends ParserRuleContext {
		public TerminalNode DECIMAL_LITERAL() { return getToken(decafJavierParser.DECIMAL_LITERAL, 0); }
		public TerminalNode HEX_LITERAL() { return getToken(decafJavierParser.HEX_LITERAL, 0); }
		public Int_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_literal; }
	}

	public final Int_literalContext int_literal() throws RecognitionException {
		Int_literalContext _localctx = new Int_literalContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_int_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			_la = _input.LA(1);
			if ( !(_la==DECIMAL_LITERAL || _la==HEX_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Rel_opContext extends ParserRuleContext {
		public TerminalNode GREATER_OP() { return getToken(decafJavierParser.GREATER_OP, 0); }
		public TerminalNode LESS_OP() { return getToken(decafJavierParser.LESS_OP, 0); }
		public TerminalNode LESS_eq_op() { return getToken(decafJavierParser.LESS_eq_op, 0); }
		public TerminalNode GREATER_eq_op() { return getToken(decafJavierParser.GREATER_eq_op, 0); }
		public Rel_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rel_op; }
	}

	public final Rel_opContext rel_op() throws RecognitionException {
		Rel_opContext _localctx = new Rel_opContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_rel_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GREATER_OP) | (1L << LESS_OP) | (1L << GREATER_eq_op) | (1L << LESS_eq_op))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Eq_opContext extends ParserRuleContext {
		public TerminalNode EQUALITY_OP() { return getToken(decafJavierParser.EQUALITY_OP, 0); }
		public TerminalNode UNEQUALITY_OP() { return getToken(decafJavierParser.UNEQUALITY_OP, 0); }
		public Eq_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eq_op; }
	}

	public final Eq_opContext eq_op() throws RecognitionException {
		Eq_opContext _localctx = new Eq_opContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_eq_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262);
			_la = _input.LA(1);
			if ( !(_la==EQUALITY_OP || _la==UNEQUALITY_OP) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Cond_opContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(decafJavierParser.AND, 0); }
		public TerminalNode OR() { return getToken(decafJavierParser.OR, 0); }
		public Cond_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond_op; }
	}

	public final Cond_opContext cond_op() throws RecognitionException {
		Cond_opContext _localctx = new Cond_opContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_cond_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==OR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public Int_literalContext int_literal() {
			return getRuleContext(Int_literalContext.class,0);
		}
		public TerminalNode CHAR_LITERAL() { return getToken(decafJavierParser.CHAR_LITERAL, 0); }
		public TerminalNode BOOL_LITERAL() { return getToken(decafJavierParser.BOOL_LITERAL, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_literal);
		try {
			setState(269);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECIMAL_LITERAL:
			case HEX_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(266);
				int_literal();
				}
				break;
			case CHAR_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(267);
				match(CHAR_LITERAL);
				}
				break;
			case BOOL_LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(268);
				match(BOOL_LITERAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Bin_opContext extends ParserRuleContext {
		public Arith_opContext arith_op() {
			return getRuleContext(Arith_opContext.class,0);
		}
		public Rel_opContext rel_op() {
			return getRuleContext(Rel_opContext.class,0);
		}
		public Eq_opContext eq_op() {
			return getRuleContext(Eq_opContext.class,0);
		}
		public Cond_opContext cond_op() {
			return getRuleContext(Cond_opContext.class,0);
		}
		public Bin_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bin_op; }
	}

	public final Bin_opContext bin_op() throws RecognitionException {
		Bin_opContext _localctx = new Bin_opContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_bin_op);
		try {
			setState(275);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD:
			case SUB:
			case MULTIPLY:
			case DIVIDE:
			case REMINDER:
				enterOuterAlt(_localctx, 1);
				{
				setState(271);
				arith_op();
				}
				break;
			case GREATER_OP:
			case LESS_OP:
			case GREATER_eq_op:
			case LESS_eq_op:
				enterOuterAlt(_localctx, 2);
				{
				setState(272);
				rel_op();
				}
				break;
			case EQUALITY_OP:
			case UNEQUALITY_OP:
				enterOuterAlt(_localctx, 3);
				{
				setState(273);
				eq_op();
				}
				break;
			case AND:
			case OR:
				enterOuterAlt(_localctx, 4);
				{
				setState(274);
				cond_op();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arith_opContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(decafJavierParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(decafJavierParser.SUB, 0); }
		public TerminalNode MULTIPLY() { return getToken(decafJavierParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(decafJavierParser.DIVIDE, 0); }
		public TerminalNode REMINDER() { return getToken(decafJavierParser.REMINDER, 0); }
		public Arith_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op; }
	}

	public final Arith_opContext arith_op() throws RecognitionException {
		Arith_opContext _localctx = new Arith_opContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_arith_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADD) | (1L << SUB) | (1L << MULTIPLY) | (1L << DIVIDE) | (1L << REMINDER))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_typeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(decafJavierParser.INT, 0); }
		public TerminalNode BOOLEAN() { return getToken(decafJavierParser.BOOLEAN, 0); }
		public Var_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_type; }
	}

	public final Var_typeContext var_type() throws RecognitionException {
		Var_typeContext _localctx = new Var_typeContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_var_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(279);
			_la = _input.LA(1);
			if ( !(_la==BOOLEAN || _la==INT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_opContext extends ParserRuleContext {
		public TerminalNode EQUAL_OP() { return getToken(decafJavierParser.EQUAL_OP, 0); }
		public TerminalNode ADD_eq_op() { return getToken(decafJavierParser.ADD_eq_op, 0); }
		public TerminalNode SUB_eq_op() { return getToken(decafJavierParser.SUB_eq_op, 0); }
		public Assign_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_op; }
	}

	public final Assign_opContext assign_op() throws RecognitionException {
		Assign_opContext _localctx = new Assign_opContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_assign_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(281);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL_OP) | (1L << ADD_eq_op) | (1L << SUB_eq_op))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_nameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(decafJavierParser.ID, 0); }
		public Method_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_name; }
	}

	public final Method_nameContext method_name() throws RecognitionException {
		Method_nameContext _localctx = new Method_nameContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_method_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 12:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;\u0120\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\2\7\29\n\2\f\2\16\2<\13\2\3\2\7\2?\n\2\f\2\16"+
		"\2B\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3M\n\3\f\3\16\3P\13\3\3"+
		"\3\3\3\3\4\3\4\3\4\3\4\7\4X\n\4\f\4\16\4[\13\4\3\4\3\4\3\5\3\5\3\5\3\5"+
		"\3\5\3\6\3\6\5\6f\n\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\7\bt\n\b\f\b\16\bw\13\b\5\by\n\b\3\b\3\b\3\b\3\t\3\t\5\t\u0080\n\t\3"+
		"\n\3\n\7\n\u0084\n\n\f\n\16\n\u0087\13\n\3\n\7\n\u008a\n\n\f\n\16\n\u008d"+
		"\13\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a2\n\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00b1\n\13\3\13\3\13\3\13"+
		"\3\13\5\13\u00b7\n\13\3\13\5\13\u00ba\n\13\3\13\3\13\3\13\3\13\5\13\u00c0"+
		"\n\13\3\f\3\f\3\f\3\f\3\f\7\f\u00c7\n\f\f\f\16\f\u00ca\13\f\5\f\u00cc"+
		"\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00db\n\r"+
		"\f\r\16\r\u00de\13\r\5\r\u00e0\n\r\3\r\3\r\5\r\u00e4\n\r\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00f2\n\16\3\16\3\16"+
		"\3\16\3\16\7\16\u00f8\n\16\f\16\16\16\u00fb\13\16\3\17\3\17\5\17\u00ff"+
		"\n\17\3\20\3\20\5\20\u0103\n\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24"+
		"\3\25\3\25\3\25\5\25\u0110\n\25\3\26\3\26\3\26\3\26\5\26\u0116\n\26\3"+
		"\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\2\3\32\33\2\4\6\b\n\f\16\20"+
		"\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\t\4\2\61\61\63\63\3\2%(\3\2,-\3"+
		"\2\"#\3\2\35!\4\2\13\13\r\r\3\2)+\2\u012e\2\64\3\2\2\2\4E\3\2\2\2\6S\3"+
		"\2\2\2\b^\3\2\2\2\ne\3\2\2\2\fg\3\2\2\2\16i\3\2\2\2\20\177\3\2\2\2\22"+
		"\u0081\3\2\2\2\24\u00bf\3\2\2\2\26\u00c1\3\2\2\2\30\u00e3\3\2\2\2\32\u00f1"+
		"\3\2\2\2\34\u00fe\3\2\2\2\36\u0102\3\2\2\2 \u0104\3\2\2\2\"\u0106\3\2"+
		"\2\2$\u0108\3\2\2\2&\u010a\3\2\2\2(\u010f\3\2\2\2*\u0115\3\2\2\2,\u0117"+
		"\3\2\2\2.\u0119\3\2\2\2\60\u011b\3\2\2\2\62\u011d\3\2\2\2\64\65\7\3\2"+
		"\2\65\66\7\4\2\2\66:\7\24\2\2\679\5\6\4\28\67\3\2\2\29<\3\2\2\2:8\3\2"+
		"\2\2:;\3\2\2\2;@\3\2\2\2<:\3\2\2\2=?\5\16\b\2>=\3\2\2\2?B\3\2\2\2@>\3"+
		"\2\2\2@A\3\2\2\2AC\3\2\2\2B@\3\2\2\2CD\7\25\2\2D\3\3\2\2\2EF\5.\30\2F"+
		"G\5\n\6\2GN\3\2\2\2HI\7\32\2\2IJ\5.\30\2JK\5\n\6\2KM\3\2\2\2LH\3\2\2\2"+
		"MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PN\3\2\2\2QR\7\23\2\2R\5\3\2\2"+
		"\2ST\5.\30\2TY\5\n\6\2UV\7\32\2\2VX\5\n\6\2WU\3\2\2\2X[\3\2\2\2YW\3\2"+
		"\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\7\23\2\2]\7\3\2\2\2^_\7.\2\2_`"+
		"\7\26\2\2`a\5 \21\2ab\7\27\2\2b\t\3\2\2\2cf\5\f\7\2df\5\b\5\2ec\3\2\2"+
		"\2ed\3\2\2\2f\13\3\2\2\2gh\7.\2\2h\r\3\2\2\2ij\5\20\t\2jk\5\62\32\2kx"+
		"\7\30\2\2lm\5.\30\2mn\5\f\7\2nu\3\2\2\2op\7\32\2\2pq\5.\30\2qr\5\f\7\2"+
		"rt\3\2\2\2so\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2vy\3\2\2\2wu\3\2\2\2"+
		"xl\3\2\2\2xy\3\2\2\2yz\3\2\2\2z{\7\31\2\2{|\5\22\n\2|\17\3\2\2\2}\u0080"+
		"\5.\30\2~\u0080\7\21\2\2\177}\3\2\2\2\177~\3\2\2\2\u0080\21\3\2\2\2\u0081"+
		"\u0085\7\24\2\2\u0082\u0084\5\4\3\2\u0083\u0082\3\2\2\2\u0084\u0087\3"+
		"\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u008b\3\2\2\2\u0087"+
		"\u0085\3\2\2\2\u0088\u008a\5\24\13\2\u0089\u0088\3\2\2\2\u008a\u008d\3"+
		"\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d"+
		"\u008b\3\2\2\2\u008e\u008f\7\25\2\2\u008f\23\3\2\2\2\u0090\u0091\5\34"+
		"\17\2\u0091\u0092\5\60\31\2\u0092\u0093\5\32\16\2\u0093\u00c0\3\2\2\2"+
		"\u0094\u0095\5\34\17\2\u0095\u0096\5\60\31\2\u0096\u0097\5\32\16\2\u0097"+
		"\u0098\7\23\2\2\u0098\u00c0\3\2\2\2\u0099\u00c0\5\30\r\2\u009a\u009b\7"+
		"\5\2\2\u009b\u009c\7\30\2\2\u009c\u009d\5\32\16\2\u009d\u009e\7\31\2\2"+
		"\u009e\u00a1\5\22\n\2\u009f\u00a0\7\6\2\2\u00a0\u00a2\5\22\n\2\u00a1\u009f"+
		"\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00c0\3\2\2\2\u00a3\u00a4\5\f\7\2\u00a4"+
		"\u00a5\7)\2\2\u00a5\u00a6\5\32\16\2\u00a6\u00a7\7\23\2\2\u00a7\u00c0\3"+
		"\2\2\2\u00a8\u00a9\7\b\2\2\u00a9\u00aa\5\32\16\2\u00aa\u00ab\7\23\2\2"+
		"\u00ab\u00c0\3\2\2\2\u00ac\u00ad\7\7\2\2\u00ad\u00b0\5\f\7\2\u00ae\u00af"+
		"\7)\2\2\u00af\u00b1\5 \21\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1"+
		"\u00b2\3\2\2\2\u00b2\u00b9\7\32\2\2\u00b3\u00b6\5\f\7\2\u00b4\u00b5\7"+
		")\2\2\u00b5\u00b7\5 \21\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7"+
		"\u00ba\3\2\2\2\u00b8\u00ba\5 \21\2\u00b9\u00b3\3\2\2\2\u00b9\u00b8\3\2"+
		"\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\5\22\n\2\u00bc\u00c0\3\2\2\2\u00bd"+
		"\u00be\7\t\2\2\u00be\u00c0\7\23\2\2\u00bf\u0090\3\2\2\2\u00bf\u0094\3"+
		"\2\2\2\u00bf\u0099\3\2\2\2\u00bf\u009a\3\2\2\2\u00bf\u00a3\3\2\2\2\u00bf"+
		"\u00a8\3\2\2\2\u00bf\u00ac\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\25\3\2\2"+
		"\2\u00c1\u00c2\5\62\32\2\u00c2\u00cb\7\30\2\2\u00c3\u00c8\5\32\16\2\u00c4"+
		"\u00c5\7\32\2\2\u00c5\u00c7\5\32\16\2\u00c6\u00c4\3\2\2\2\u00c7\u00ca"+
		"\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca"+
		"\u00c8\3\2\2\2\u00cb\u00c3\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2"+
		"\2\2\u00cd\u00ce\7\31\2\2\u00ce\27\3\2\2\2\u00cf\u00e4\5\26\f\2\u00d0"+
		"\u00d1\5\26\f\2\u00d1\u00d2\7\23\2\2\u00d2\u00e4\3\2\2\2\u00d3\u00d4\7"+
		"\22\2\2\u00d4\u00d5\7\30\2\2\u00d5\u00df\7\65\2\2\u00d6\u00d7\7\32\2\2"+
		"\u00d7\u00dc\5\36\20\2\u00d8\u00d9\7\32\2\2\u00d9\u00db\5\36\20\2\u00da"+
		"\u00d8\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2"+
		"\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00d6\3\2\2\2\u00df"+
		"\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\7\31\2\2\u00e2\u00e4\7"+
		"\23\2\2\u00e3\u00cf\3\2\2\2\u00e3\u00d0\3\2\2\2\u00e3\u00d3\3\2\2\2\u00e4"+
		"\31\3\2\2\2\u00e5\u00e6\b\16\1\2\u00e6\u00f2\5\34\17\2\u00e7\u00f2\5("+
		"\25\2\u00e8\u00e9\7\36\2\2\u00e9\u00f2\5\32\16\6\u00ea\u00f2\5\30\r\2"+
		"\u00eb\u00ec\7$\2\2\u00ec\u00f2\5\32\16\4\u00ed\u00ee\7\30\2\2\u00ee\u00ef"+
		"\5\32\16\2\u00ef\u00f0\7\31\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00e5\3\2\2"+
		"\2\u00f1\u00e7\3\2\2\2\u00f1\u00e8\3\2\2\2\u00f1\u00ea\3\2\2\2\u00f1\u00eb"+
		"\3\2\2\2\u00f1\u00ed\3\2\2\2\u00f2\u00f9\3\2\2\2\u00f3\u00f4\f\7\2\2\u00f4"+
		"\u00f5\5*\26\2\u00f5\u00f6\5\32\16\b\u00f6\u00f8\3\2\2\2\u00f7\u00f3\3"+
		"\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa"+
		"\33\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00ff\5\f\7\2\u00fd\u00ff\5\b\5"+
		"\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\35\3\2\2\2\u0100\u0103"+
		"\5\32\16\2\u0101\u0103\7\65\2\2\u0102\u0100\3\2\2\2\u0102\u0101\3\2\2"+
		"\2\u0103\37\3\2\2\2\u0104\u0105\t\2\2\2\u0105!\3\2\2\2\u0106\u0107\t\3"+
		"\2\2\u0107#\3\2\2\2\u0108\u0109\t\4\2\2\u0109%\3\2\2\2\u010a\u010b\t\5"+
		"\2\2\u010b\'\3\2\2\2\u010c\u0110\5 \21\2\u010d\u0110\7\60\2\2\u010e\u0110"+
		"\7\64\2\2\u010f\u010c\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u010e\3\2\2\2"+
		"\u0110)\3\2\2\2\u0111\u0116\5,\27\2\u0112\u0116\5\"\22\2\u0113\u0116\5"+
		"$\23\2\u0114\u0116\5&\24\2\u0115\u0111\3\2\2\2\u0115\u0112\3\2\2\2\u0115"+
		"\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116+\3\2\2\2\u0117\u0118\t\6\2\2"+
		"\u0118-\3\2\2\2\u0119\u011a\t\7\2\2\u011a/\3\2\2\2\u011b\u011c\t\b\2\2"+
		"\u011c\61\3\2\2\2\u011d\u011e\7.\2\2\u011e\63\3\2\2\2\34:@NYeux\177\u0085"+
		"\u008b\u00a1\u00b0\u00b6\u00b9\u00bf\u00c8\u00cb\u00dc\u00df\u00e3\u00f1"+
		"\u00f9\u00fe\u0102\u010f\u0115";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}