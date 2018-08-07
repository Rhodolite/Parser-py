#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ParseExpressionStatement')
def module():
    require_module('PythonParser.TokenizeOperator')
    require_module('PythonParser.BookcaseManyStatement')


    def parse_PYTHON__statement_assign__left__equal_sign(indented, left, equal_sign):
        right = parse_PYTHON__ternary_expression_list()

        operator = qk()

        if operator is not 0:
            wk0()
        else:
            newline = qn()

            if newline is not 0:
                return conjure_assign_1(conjure_indentation(indented), left, equal_sign, right, newline)

            operator = tokenize_PYTHON_operator()

        if not operator.is_equal_sign:
            #my_line('indented: %r; left: %r; equal_sign: %r; right: %s; operator: %r; s: %s',
            #        indented, left, equal_sign, right, operator, portray_string(qs()[qj():]))

            raise_unknown_line()

        many       = [left, right]
        many_frill = [equal_sign, operator]

        while 7 is 7:
            many.append(parse_PYTHON__ternary_expression_list())

            operator = qk()

            if operator is not 0:
                wk0()
            else:
                newline = qn()

                if newline is not 0:
                    return conjure_assign_many(conjure_indentation(indented), many, many_frill, newline)

                operator = tokenize_PYTHON_operator()

            if not operator.is_equal_sign:
                #my_line('right: %s; operator; %r; s: %s', right, operator, portray_string(qs()[qj():]))
                raise_unknown_line()

            many_frill.append(operator)


    def parse_PYTHON__statement_modify__left__operator(indented, left, modify_operator):
        right = parse_PYTHON__ternary_expression_list()

        newline = qn()

        if newline is not 0:
            return conjure_modify_statement(conjure_indentation(indented), left, modify_operator, right, newline)

        #my_line('indented: %r; left: %r; modify_operator: %r; right: %s; s: %s',
        #        indented, left, modify_operator, right, portray_string(qs()[qj():]))

        raise_unknown_line()


    @share
    def parse_PYTHON__statement_expression__atom(indented, left):
        indentation = conjure_indentation(indented)

        if left.is_CRYSTAL_atom:
            pass
        elif left.is_keyword_not:
            left = parse_PYTHON__not_expression__operator(left)
        elif left.is_minus_sign:
            left = parse_PYTHON__negative_expression__operator(left)
        elif left.is_left_parenthesis:
            left = parse_PYTHON__parenthesized_expression__left_parenthesis(left)
        elif left.is_left_square_bracket:
            left = parse_PYTHON__list_expression__left_square_bracket(left)
        else:
            raise_unknown_line()

        operator = qk()

        if operator is not 0:
            wk0()
        else:
            newline = qn()

            if newline is not 0:
                return conjure_expression_statement(conjure_indentation(indented), left, newline)

            operator = tokenize_PYTHON_operator()

        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator, indentation)

            if left.is_statement:
                return left

            operator = qk()

            if operator is 0:
                newline = qn()

                if newline is not 0:
                    return conjure_expression_statement(conjure_indentation(indented), left, newline)

                raise_unknown_line()

            wk0()

        if not operator.is_end_of_ternary_expression_list:
            left = parse_PYTHON__ternary_expression_list__X_any_expression(left, operator)

            operator = qk()

            if operator is 0:
                newline = qn()

                if newline is not 0:
                    return conjure_expression_statement(conjure_indentation(indented), left, newline)

                raise_unknown_line()

            wk0()

        if operator.is_equal_sign:
            return parse_PYTHON__statement_assign__left__equal_sign(indented, left, operator)

        if operator.is_modify_operator:
            return parse_PYTHON__statement_modify__left__operator(indented, left, operator)

        #my_line('line: %d; operator: %s', ql(), operator)
        raise_unknown_line()
