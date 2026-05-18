from ast_nodes import SymbolTable, ProgramNode, LambdaNode, ParamNode, BinaryOpNode, VariableNode, LiteralNode

class LexicalAnalyzer:
    def __init__(self):
        self.keywords = {'auto', 'int', 'float', 'return'}
        
    def analyze(self, text: str):
        lexemes = []
        errors = []
        
        row = 1
        col = 1
        
        state = 'START'
        buffer = ''
        start_col = 1
        
        i = 0
        text_len = len(text)
        
        while i < text_len:
            char = text[i]
            
            if state == 'START':
                buffer = ''
                start_col = col
                
                if char.isspace():
                    state = 'SPACE'
                    buffer += char
                elif char.isalpha() or char == '_':
                    state = 'IDENTIFIER'
                    buffer += char
                elif char.isdigit():
                    state = 'NUMBER'
                    buffer += char
                elif char == '+':
                    state = 'PLUS'
                    buffer += char
                elif char == '-':
                    state = 'MINUS'
                    buffer += char
                elif char == '*':
                    state = 'MULTIPLY'
                    buffer += char
                elif char == '/':
                    state = 'DIVIDE'
                    buffer += char
                elif char == '=':
                    state = 'ASSIGN'
                    buffer += char
                elif char == '[':
                    lexemes.append({'code': 5, 'type': 'Спецсимвол', 'lexeme': char, 'row': row, 'start_col': start_col, 'end_col': start_col})
                elif char == ']':
                    lexemes.append({'code': 6, 'type': 'Спецсимвол', 'lexeme': char, 'row': row, 'start_col': start_col, 'end_col': start_col})
                elif char == '(':
                    lexemes.append({'code': 7, 'type': 'Спецсимвол', 'lexeme': char, 'row': row, 'start_col': start_col, 'end_col': start_col})
                elif char == ')':
                    lexemes.append({'code': 8, 'type': 'Спецсимвол', 'lexeme': char, 'row': row, 'start_col': start_col, 'end_col': start_col})
                elif char == '{':
                    lexemes.append({'code': 9, 'type': 'Спецсимвол', 'lexeme': char, 'row': row, 'start_col': start_col, 'end_col': start_col})
                elif char == '}':
                    lexemes.append({'code': 10, 'type': 'Спецсимвол', 'lexeme': char, 'row': row, 'start_col': start_col, 'end_col': start_col})
                elif char == ',':
                    lexemes.append({'code': 11, 'type': 'Спецсимвол', 'lexeme': char, 'row': row, 'start_col': start_col, 'end_col': start_col})
                elif char == ';':
                    lexemes.append({'code': 12, 'type': 'Спецсимвол', 'lexeme': char, 'row': row, 'start_col': start_col, 'end_col': start_col})
                else:
                    state = 'ERROR'
                    buffer += char
                
                if state == 'START':
                    pass

            elif state == 'SPACE':
                if char.isspace():
                    buffer += char
                else:
                    lexemes.append({'code': 13, 'type': 'Разделитель', 'lexeme': buffer.replace('\n', '\\n').replace('\t', '\\t'), 'row': row, 'start_col': start_col, 'end_col': col - 1})
                    state = 'START'
                    i -= 1
                    col -= 1

            elif state == 'IDENTIFIER':
                if char.isalnum() or char == '_':
                    buffer += char
                else:
                    if buffer in self.keywords:
                        code = 3
                        l_type = 'Ключевое слово'
                    else:
                        code = 2
                        l_type = 'Идентификатор'
                    lexemes.append({'code': code, 'type': l_type, 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': col - 1})
                    state = 'START'
                    i -= 1
                    col -= 1

            elif state == 'NUMBER':
                if char.isdigit():
                    buffer += char
                else:
                    lexemes.append({'code': 1, 'type': 'Целое без знака', 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': col - 1})
                    state = 'START'
                    i -= 1
                    col -= 1

            elif state == 'PLUS':
                lexemes.append({'code': 4, 'type': 'Оператор', 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': start_col})
                state = 'START'
                i -= 1
                col -= 1
                
            elif state == 'MINUS':
                lexemes.append({'code': 4, 'type': 'Оператор', 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': start_col})
                state = 'START'
                i -= 1
                col -= 1

            elif state == 'MULTIPLY':
                lexemes.append({'code': 4, 'type': 'Оператор', 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': start_col})
                state = 'START'
                i -= 1
                col -= 1

            elif state == 'DIVIDE':
                lexemes.append({'code': 4, 'type': 'Оператор', 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': start_col})
                state = 'START'
                i -= 1
                col -= 1
                
            elif state == 'ASSIGN':
                lexemes.append({'code': 4, 'type': 'Оператор', 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': start_col})
                state = 'START'
                i -= 1
                col -= 1

            elif state == 'ERROR':
                errors.append({'code': 99, 'type': 'Недопустимый символ', 'lexeme': buffer, 'row': row, 'col': start_col, 'start_col': start_col, 'end_col': start_col, 'message': f"Недопустимый символ '{buffer}'"})
                lexemes.append({'code': 99, 'type': 'Недопустимый символ', 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': start_col})
                state = 'START'
                i -= 1
                col -= 1

            if char == '\n':
                if state != 'SPACE':
                    row += 1
                    col = 0
                else:
                    pass 
            
            if char == '\n' and state == 'SPACE':
                row += 1
                col = 0
            
            i += 1
            col += 1

        if state == 'SPACE':
             lexemes.append({'code': 13, 'type': 'Разделитель', 'lexeme': buffer.replace('\n', '\\n').replace('\t', '\\t'), 'row': row, 'start_col': start_col, 'end_col': col - 1})
        elif state == 'IDENTIFIER':
            if buffer in self.keywords:
                code = 3
                l_type = 'Ключевое слово'
            else:
                code = 2
                l_type = 'Идентификатор'
            lexemes.append({'code': code, 'type': l_type, 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': col - 1})
        elif state == 'NUMBER':
            lexemes.append({'code': 1, 'type': 'Целое без знака', 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': col - 1})
        elif state in ('PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'ASSIGN'):
            lexemes.append({'code': 4, 'type': 'Оператор', 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': start_col})
        elif state == 'ERROR':
            errors.append({'code': 99, 'type': 'Недопустимый символ', 'lexeme': buffer, 'row': row, 'col': start_col, 'start_col': start_col, 'end_col': start_col, 'message': f"Недопустимый символ '{buffer}'"})
            lexemes.append({'code': 99, 'type': 'Недопустимый символ', 'lexeme': buffer, 'row': row, 'start_col': start_col, 'end_col': start_col})

        return lexemes, errors

class SyntaxAnalyzer:
    def __init__(self, lexemes):
        self.raw_lexemes = [l for l in lexemes if l['code'] != 13]
        self.lexemes = [l for l in lexemes if l['code'] != 13 and l['code'] != 99]
        self.pos = 0
        self.errors = []
        self.symbol_table = SymbolTable()
        self.ast_root = None
        
    def current(self):
        if self.pos < len(self.lexemes):
            return self.lexemes[self.pos]
        return None

    def advance(self):
        self.pos += 1

    def match(self, expected_lexeme, sync_set):
        curr = self.current()
        if curr and curr['lexeme'] == expected_lexeme:
            self.advance()
            return True
        else:
            self.report_error(f"Ожидалось '{expected_lexeme}'", curr)
            self.neutralize(sync_set)
            return False

    def match_type(self, expected_type, sync_set):
        curr = self.current()
        if curr and curr['type'] == expected_type:
            self.advance()
            return True
        else:
            self.report_error(f"Ожидался тип лексемы '{expected_type}'", curr)
            self.neutralize(sync_set)
            return False

    def report_error(self, message, lexeme):
        if lexeme:
            self.errors.append({
                "lexeme": lexeme['lexeme'],
                "row": lexeme['row'],
                "col": lexeme['start_col'],
                "message": message
            })
        else:
            self.errors.append({
                "lexeme": "EOF",
                "row": "-",
                "col": "-",
                "message": message
            })

    def neutralize(self, sync_set):
        while self.current():
            curr = self.current()
            if curr['lexeme'] in sync_set or curr['type'] in sync_set:
                return
            self.advance()

    def parse(self):
        if not self.lexemes:
            self.report_error("Пустой файл или отсутствуют значимые лексемы", None)
            return None, self.errors
            
        self.ast_root = self.parse_Program()
        if self.pos < len(self.lexemes):
            self.report_error("Неожиданные символы в конце файла", self.current())
            
        return self.ast_root, self.errors

    def parse_Program(self):
        sync = {';', '}'}
        if not self.match('auto', sync.union({'Идентификатор', '=', '{', '['})):
            while self.pos + 1 < len(self.lexemes):
                curr = self.lexemes[self.pos]
                nxt = self.lexemes[self.pos + 1]
                if curr['type'] == 'Идентификатор' and nxt['lexeme'] in ('=', '{'):
                    break
                if curr['lexeme'] in ('=', '{', '['):
                    break
                self.advance()
        
        curr = self.current()
        name = curr['lexeme'] if curr else "unknown"
        if curr:
            self.symbol_table.declare(name, 'lambda', curr['row'], curr['start_col'])
            
        self.match_type('Идентификатор', sync.union({'=', '{', '['}))
        init_node = self.parse_Init(sync)
        return ProgramNode(name, init_node)

    def parse_Init(self, sync_set):
        curr = self.current()
        node = None
        if curr and curr['lexeme'] == '=':
            self.match('=', {'['}.union(sync_set))
            node = self.parse_Lambda(sync_set.union({';'}))
            self.match(';', sync_set)
        elif curr and curr['lexeme'] == '{':
            self.match('{', {'['}.union(sync_set))
            node = self.parse_Lambda(sync_set.union({'}'}))
            self.match('}', {';'}.union(sync_set))
            self.match(';', sync_set)
        else:
            self.report_error("Ожидалось '=' или '{' для инициализации", curr)
            self.neutralize(sync_set.union({'=', '{', '['}))
            curr2 = self.current()
            if curr2 and curr2['lexeme'] == '=':
                self.match('=', {'['}.union(sync_set))
                node = self.parse_Lambda(sync_set.union({';'}))
                self.match(';', sync_set)
            elif curr2 and curr2['lexeme'] == '{':
                self.match('{', {'['}.union(sync_set))
                node = self.parse_Lambda(sync_set.union({'}'}))
                self.match('}', {';'}.union(sync_set))
                self.match(';', sync_set)
            elif curr2 and curr2['lexeme'] == '[':
                node = self.parse_Lambda(sync_set.union({';'}))
                self.match(';', sync_set)
        return node

    def parse_Lambda(self, sync_set):
        self.match('[', {']', '(', 'int', 'float', ')', '{', 'return', '}'}.union(sync_set))
        self.match(']', {'(', 'int', 'float', ')', '{', 'return', '}'}.union(sync_set))
        self.match('(', {'int', 'float', ')', '{', 'return', '}'}.union(sync_set))
        
        params = []
        self.parse_ArgList({')', '{', 'return', '}'}.union(sync_set), params)
        
        self.match(')', {'{', 'return', 'Идентификатор', 'Целое без знака', '(', '}'}.union(sync_set))
        self.match('{', {'return', 'Идентификатор', 'Целое без знака', '(', '}'}.union(sync_set))
        
        if not self.match('return', {'Идентификатор', 'Целое без знака', '(', ';', '}'}.union(sync_set)):
            self.skip_touching_garbage()
                
        body = self.parse_Expression({';', '}'}.union(sync_set))
        
        curr = self.current()
        if curr and curr['lexeme'] not in (';', '}'):
            if curr['lexeme'] == ')':
                self.report_error("Нарушен баланс скобок: лишняя ')'", curr)
            else:
                self.report_error("Пропущен арифметический оператор или ';'", curr)
            self.neutralize({';', '}'}.union(sync_set))
            
        self.match(';', {'}'}.union(sync_set))
        self.match('}', sync_set)
        
        return LambdaNode(params, body)

    def _is_arg_start(self):
        curr = self.current()
        return (curr and curr['lexeme'] in ('int', 'float')) or \
               (curr and curr['type'] == 'Идентификатор')

    def parse_ArgList(self, sync_set, params):
        if self._is_arg_start():
            param_type = self.parse_Type({'Идентификатор', 'int', 'float'}.union(sync_set))
            name, curr_tok = self._match_param_name(sync_set)
            
            if name:
                if not self.symbol_table.declare(name, param_type, curr_tok['row'], curr_tok['start_col']):
                    self.report_error(f'Ошибка: идентификатор "{name}" уже объявлен ранее', curr_tok)
                params.append(ParamNode(param_type, name))
                
            self.parse_ArgListTail(sync_set, params, suppress_comma_error=not bool(name)) 

    def _match_param_name(self, sync_set):
        curr = self.current()
        if curr and curr['type'] == 'Идентификатор':
            name = curr['lexeme']
            self.advance()
            return name, curr
        else:
            self.report_error("Ожидалось имя параметра (идентификатор)", curr)
            self.neutralize(sync_set)
            return None, curr

    def are_lexemes_touching(self, lex1, lex2):
        try:
            start_idx = self.raw_lexemes.index(lex1)
            end_idx = self.raw_lexemes.index(lex2)
        except ValueError:
            return False
            
        for i in range(start_idx, end_idx):
            if self.raw_lexemes[i+1]['start_col'] > self.raw_lexemes[i]['end_col'] + 1:
                return False
        return True

    def skip_touching_garbage(self):
        while True:
            curr = self.current()
            if not curr:
                break
            if curr['type'] == 'Идентификатор':
                self.advance()
                nxt = self.current()
                if nxt and nxt['type'] == 'Идентификатор':
                    if self.are_lexemes_touching(curr, nxt):
                        continue
                    else:
                        break
                else:
                    break
            else:
                break

    def parse_ArgListTail(self, sync_set, params, suppress_comma_error=False):
        curr = self.current()
        
        if curr and curr['lexeme'] == ',':
            self.match(',', {'int', 'float'}.union(sync_set))
            
            if self._is_arg_start():
                param_type = self.parse_Type({'Идентификатор', 'int', 'float'}.union(sync_set))
                name, curr_tok = self._match_param_name(sync_set)
                
                if name:
                    if not self.symbol_table.declare(name, param_type, curr_tok['row'], curr_tok['start_col']):
                        self.report_error(f'Ошибка: идентификатор "{name}" уже объявлен ранее', curr_tok)
                    params.append(ParamNode(param_type, name))
                    
                self.parse_ArgListTail(sync_set, params, suppress_comma_error=not bool(name))
            else:
                self.report_error("Ожидался аргумент после ','", curr)
                
        elif self._is_arg_start():
            if not suppress_comma_error:
                self.report_error("Ожидалось ','", curr)
            param_type = self.parse_Type({'Идентификатор', 'int', 'float'}.union(sync_set))
            name, curr_tok = self._match_param_name(sync_set)
            
            if name:
                if not self.symbol_table.declare(name, param_type, curr_tok['row'], curr_tok['start_col']):
                    self.report_error(f'Ошибка: идентификатор "{name}" уже объявлен ранее', curr_tok)
                params.append(ParamNode(param_type, name))
                
            self.parse_ArgListTail(sync_set, params, suppress_comma_error=not bool(name))
            
        else:
            pass

    def parse_Type(self, sync_set):
        curr = self.current()
        param_type = "unknown"
        if curr and curr['lexeme'] in ('int', 'float'):
            param_type = curr['lexeme']
            self.advance()
        else:
            self.report_error("Ожидался тип данных (int, float)", curr)
            self.skip_touching_garbage()
        return param_type

    def parse_Expression(self, sync_set):
        left = self.parse_Term(sync_set.union({'+', '-'}))
        return self.parse_ExpTail(sync_set, left)

    def parse_ExpTail(self, sync_set, left):
        curr = self.current()
        if curr and curr['lexeme'] in ('+', '-'):
            op = self.parse_AddOp({'Идентификатор', 'Целое без знака', '('}.union(sync_set))
            right = self.parse_Term(sync_set.union({'+', '-'}))
            new_left = BinaryOpNode(op, left, right)
            return self.parse_ExpTail(sync_set, new_left)
        else:
            return left

    def parse_AddOp(self, sync_set):
        curr = self.current()
        op = "+"
        if curr and curr['lexeme'] in ('+', '-'):
            op = curr['lexeme']
            self.advance()
        else:
            self.report_error("Ожидался оператор сложения/вычитания", curr)
            self.neutralize(sync_set)
        return op

    def parse_Term(self, sync_set):
        left = self.parse_Factor(sync_set.union({'*', '/'}))
        return self.parse_TermTail(sync_set, left)

    def parse_TermTail(self, sync_set, left):
        curr = self.current()
        if curr and curr['lexeme'] in ('*', '/'):
            op = self.parse_MultOp({'Идентификатор', 'Целое без знака', '('}.union(sync_set))
            right = self.parse_Factor(sync_set.union({'*', '/'}))
            new_left = BinaryOpNode(op, left, right)
            return self.parse_TermTail(sync_set, new_left)
        else:
            return left

    def parse_MultOp(self, sync_set):
        curr = self.current()
        op = "*"
        if curr and curr['lexeme'] in ('*', '/'):
            op = curr['lexeme']
            self.advance()
        else:
            self.report_error("Ожидался оператор умножения/деления", curr)
            self.neutralize(sync_set)
        return op

    def parse_Factor(self, sync_set):
        curr = self.current()
        node = None
        if curr and curr['type'] == 'Идентификатор':
            name = curr['lexeme']
            if not self.symbol_table.lookup(name):
                self.report_error(f'Ошибка: идентификатор "{name}" не был объявлен ранее', curr)
            node = VariableNode(name)
            self.advance()
        elif curr and curr['type'] == 'Целое без знака':
            val_str = curr['lexeme']
            try:
                val = int(val_str)
                if val > 2147483647:
                    self.report_error(f'Ошибка: значение {val} превышает допустимый предел для int', curr)
            except ValueError:
                self.report_error(f'Ошибка: некорректное числовое значение', curr)
            node = LiteralNode(val_str)
            self.advance()
        elif curr and curr['lexeme'] == '(':
            self.match('(', {'Идентификатор', 'Целое без знака', '('}.union(sync_set))
            node = self.parse_Expression(sync_set.union({')'}))
            self.match(')', sync_set)
        else:
            self.report_error("Ожидался операнд (идентификатор, число, открывающая скобка)", curr)
            self.neutralize(sync_set)
        return node
