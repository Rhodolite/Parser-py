#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ParseSimple')
def module():
    require_module('PythonParser.BookcaseKeywordStatement')
    require_module('PythonParser.BookcaseStatement')
    require_module('PythonParser.BookcaseTriple')


    @share
    def parse_PYTHON__statement_break(m):
        if m.end('newline') is -1:
            raise_unknown_line()

        return evoke_indented__break__line_marker(m.end('indented'), m.end('atom'))


    @share
    def parse_PYTHON__statement_continue(m):
        if m.end('newline') is -1:
            raise_unknown_line()

        return evoke_indented__continue__line_marker(m.end('indented'), m.end('atom'))


    @share
    def parse_PYTHON__statement_decorator_header(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indentation__at_sign = evoke_indented__at_sign(m.end('indented'), j)

        wi(j)
        wj(j)

        name    = tokenize_name()
        newline = qn()

        if newline is not none:
            return conjure_decorator_header(indentation__at_sign, name, newline)

        operator = tokenize_PYTHON_operator()

        if operator.is_arguments_0:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return conjure_decorator_header(indentation__at_sign, conjure_call_expression(name, operator), newline)

        if not operator.is_CRYSTAL_left_parenthesis:
            raise_unknown_line()

        call = parse_PYTHON__call_expression__left__operator(name, operator)

        newline = qn()

        if newline is none:
            raise_unknown_line()

        return conjure_decorator_header(indentation__at_sign, call, newline)


    @share
    def parse_PYTHON__statement_assert(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_assert(m.end('indented'), j)

        wi(j)
        wj(j)

        left = parse_PYTHON__ternary_expression()

        operator = qk()

        if operator is 0:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return conjure_assert_statement_1(indented_keyword, left, newline)

        wk0()

        if not operator.is_CRYSTAL_comma:
            raise_unknown_line()

        right = parse_PYTHON__ternary_expression()

        operator_2 = qk()

        if operator_2 is 0:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return conjure_assert_statement_2(indented_keyword, left, operator, right, newline)

        raise_unknown_line()


    @share
    def parse_PYTHON__statement_delete(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_delete(m.end('indented'), j)

        wi(j)
        wj(j)

        left = parse_PYTHON__normal_expression()

        operator = qk()

        if operator is 0:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return conjure_delete_header(indented_keyword, left, newline)

        wk0()

        if not operator.is_CRYSTAL_comma:
            raise_unknown_line()

        many       = [left]
        many_frill = [operator]

        while 7 is 7:
            many.append(parse_PYTHON__normal_expression())

            operator = qk()

            if operator is 0:
                newline = qn()

                if newline is none:
                    raise_unknown_line()

                return conjure_delete_many(indented_keyword, many, many_frill, newline)

            wk0()

            if not operator.is_CRYSTAL_comma:
                raise_unknown_line()

            many_frill.append(operator)


    @share
    def parse_PYTHON__statement_pass(m):
        if m.end('newline') is -1:
            raise_unknown_line()

        return evoke_indented__pass__line_marker(m.end('indented'), m.end('atom'))


    @share
    def parse_PYTHON__statement_raise(m):
        if m.end('newline') is not -1:
            return evoke_indented__raise__line_marker(m.end('indented'), m.end('atom'))

        j = m.end()

        indented_keyword = evoke_indented_raise(m.end('indented'), j)

        wi(j)
        wj(j)

        left = parse_PYTHON__ternary_expression()

        operator = qk()

        if operator is 0:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return conjure_raise_statement_1(indented_keyword, left, newline)

        wk0()

        if not operator.is_CRYSTAL_comma:
            raise_unknown_line()

        middle = parse_PYTHON__ternary_expression()

        operator_2 = qk()

        if operator_2 is 0:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return conjure_raise_statement_2(indented_keyword, left, operator, middle, newline)

        wk0()

        if not operator_2.is_CRYSTAL_comma:
            raise_unknown_line()

        right = parse_PYTHON__ternary_expression()

        if qk() is 0:
            newline = qn()

            if newline is none:
                raise_unknown_line()

            return conjure_raise_statement_3(indented_keyword, left, operator, middle, operator_2, right, newline)

        raise_unknown_line()


    @share
    def parse_PYTHON__statement_return(m):
        if m.end('newline') is not -1:
            return evoke_indented__return__line_marker(m.end('indented'), m.end('atom'))

        j = m.end()

        indented_keyword = evoke_indented_return(m.end('indented'), j)

        wi(j)
        wj(j)

        right = parse_PYTHON__ternary_expression_list()

        if qk() is not 0:
            #my_line('qk: %r; full: %s', qk(), portray_string(qs()))
            raise_unknown_line()

        newline = qn()

        if newline is none:
            raise_unknown_line()

        return conjure_return_statement(indented_keyword, right, newline)


    @share
    def parse_PYTHON__statement_yield(m):
        if m.end('newline') is not -1:
            return evoke_indented__yield__line_marker(m.end('indented'), m.end('atom'))

        j = m.end()

        indented_keyword = evoke_indented_yield(m.end('indented'), j)

        wi(j)
        wj(j)

        left = parse_PYTHON__ternary_expression_list()

        if qk() is not 0:
            raise_unknown_line()

        newline = qn()

        if newline is none:
            raise_unknown_line()

        return conjure_yield_statement_1(indented_keyword, left, newline)
