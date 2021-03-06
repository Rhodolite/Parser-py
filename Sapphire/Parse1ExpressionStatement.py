#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.Parse1ExpressionStatement')
def gem():
    require_gem('Sapphire.BookcaseManyStatement')


    show = 0


    def parse1_statement_assign__left__equal_sign(indented, left, equal_sign):
        right = parse1_ternary_expression_list()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            newline = qn()

            if newline is not none:
                return conjure_assign_1(conjure_indentation(indented), left, equal_sign, right, newline)

            operator = tokenize_operator()

        if not operator.is_equal_sign:
            #my_line('indented: %r; left: %r; equal_sign: %r; right: %s; operator: %r; s: %s',
            #        indented, left, equal_sign, right, operator, portray_string(qs()[qj():]))

            raise_unknown_line()

        many       = [left, right]
        many_frill = [equal_sign, operator]

        while 7 is 7:
            many.append(parse1_ternary_expression_list())

            operator = qk()

            if operator is not none:
                wk(none)
            else:
                newline = qn()

                if newline is not none:
                    return conjure_assign_many(conjure_indentation(indented), many, many_frill, newline)

                operator = tokenize_operator()

            if not operator.is_equal_sign:
                #my_line('right: %s; operator; %r; s: %s', right, operator, portray_string(qs()[qj():]))
                raise_unknown_line()

            many_frill.append(operator)


    def parse1_statement_modify__left__operator(indented, left, modify_operator):
        right = parse1_ternary_expression_list()

        newline = qn()

        if newline is not none:
            return conjure_modify_statement(conjure_indentation(indented), left, modify_operator, right, newline)

        #my_line('indented: %r; left: %r; modify_operator: %r; right: %s; s: %s',
        #        indented, left, modify_operator, right, portray_string(qs()[qj():]))

        raise_unknown_line()


    @share
    def parse1_statement_expression__atom(indented, left):
        indentation = conjure_indentation(indented)

        if left.is_atom:
            pass
        elif left.is_keyword_not:
            left = parse1_not_expression__operator(left)
        elif left.is_minus_sign:
            left = parse1_negative_expression__operator(left)
        elif left.is_left_parenthesis:
            left = parse1__parenthesized_expression__left_parenthesis(left)
        elif left.is_left_square_bracket:
            left = parse1__list_expression__left_square_bracket(left)
        else:
            raise_unknown_line()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            newline = qn()

            if newline is not none:
                return conjure_expression_statement(conjure_indentation(indented), left, newline)

            operator = tokenize_operator()

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator, indentation)

            if left.is_statement:
                return left

            operator = qk()

            if operator is none:
                newline = qn()

                if newline is not none:
                    return conjure_expression_statement(conjure_indentation(indented), left, newline)

                raise_unknown_line()

            wk(none)

        if not operator.is_end_of_ternary_expression_list:
            left = parse1_ternary_expression_list__X_any_expresion(left, operator)

            operator = qk()

            if operator is none:
                newline = qn()

                if newline is not none:
                    return conjure_expression_statement(conjure_indentation(indented), left, newline)

                raise_unknown_line()

            wk(none)

        if operator.is_equal_sign:
            return parse1_statement_assign__left__equal_sign(indented, left, operator)

        if operator.is_modify_operator:
            return parse1_statement_modify__left__operator(indented, left, operator)

        #my_line('line: %d; operator: %s', ql(), operator)
        raise_unknown_line()
