try:
    do_somthing_what_could_throw_error()
except Type1Error:
    handle_type1_errors()
except Type2Error as err:
    handle_type2_errors(err)
except (Type3Error, Type4Error, Type5Error):
    handle_types345_errors()
except (Type6Error, Type7Error) as err:
    handle_types67_errors(err)
except:
    handle_other_errors()
else:
    handle_no_exceptions()
finally:
    do_always()