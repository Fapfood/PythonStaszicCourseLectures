except:
    handle_other_exceptions()

except Exception as err:
    handle_other_exceptions(err)

except:
    handle_additional_operations()
    raise # reraise last exception