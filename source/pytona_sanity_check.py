import inspect,importlib
import pkgutil
import os
import sys

fail_count = 0
warn_count = 0
pass_count = 0


def report_pass(statement):
    print statement
    global pass_count
    pass_count += 1


def report_warn(statement):
    print statement
    global warn_count
    warn_count += 1


def report_fail(statement):
    print statement
    global fail_count
    fail_count += 1


class ClassInfo:
    """
    stores information for 1) determining if a class exists
    2) testing whether instantiation works
    """
    def __init__(self, check_fn):
        self.present = False
        self.class_obj = None
        self.check_fn = check_fn

    def test_create(self):
        obj = self.check_fn(self.class_obj)
        return obj is not None

class_infos = {'pyTona.answer_funcs.FibSeqFinder': ClassInfo(lambda c: c()),
               'pyTona.main.Interface': ClassInfo(lambda c: c()),
               'pyTona.main.QA': ClassInfo(lambda c: c("question", "answer")),
               'pyTona.question_answer.QA': ClassInfo(lambda c: c("question", "answer"))
               }

class FunctionInfo:
    """
    used to retain information to 1) determine if a known function is present or not 2) verify it can be called
    """
    def __init__(self, check_fn):
        self.present = False
        self.fn_obj = None
        self.check_fn = check_fn

    def test_call(self):
        return self.check_fn(self.fn_obj)


function_infos = {'pyTona.answer_funcs.feet_to_miles': FunctionInfo(lambda f: f(5280) == "1.0 miles"),
                  'pyTona.answer_funcs.get_fibonacci_seq': FunctionInfo(lambda f: f(6) is not None),
                  'pyTona.answer_funcs.get_git_branch': FunctionInfo(lambda f: f()),
                  'pyTona.answer_funcs.get_git_url': FunctionInfo(lambda f: f()),
                  'pyTona.answer_funcs.get_other_users': FunctionInfo(lambda f: f()),
                  'pyTona.answer_funcs.hal_20': FunctionInfo(lambda f: f()),
                  'pyTona.main.feet_to_miles': FunctionInfo(lambda f: f(5280)=="1.0 miles"),
                  'pyTona.main.get_fibonacci_seq': FunctionInfo(lambda f: f(5) is not None),
                  'pyTona.main.get_git_branch': FunctionInfo(lambda f: f()),
                  'pyTona.main.get_git_url': FunctionInfo(lambda f: f()),
                  'pyTona.main.get_other_users': FunctionInfo(lambda f: f()),
                  'pyTona.main.hal_20': FunctionInfo(lambda f: f())
               }

def check_package(pkg_path):
    """
    Used to check the package can be imported, and the dependent modules can be loaded too
    :param pkg_path:
    :return:
    """
    pkg_name = os.path.split(pkg_path[0])[1]
    importer = pkgutil.get_importer(pkg_path[0])
    if importer is not None:
        report_pass("package %s found" % pkg_name)
    else:
        report_fail("fatal error: cannot load package %s" % pkg_name)
        return
    for importer, modname, ispkg in pkgutil.iter_modules(pkg_path):
        #print "Found submodule %s (is a package: %s)" % (modname, ispkg)
        check_imports(os.path.split(importer.path)[1] + "." + modname)

def check_imports(modname):
    """
    Checks if the modules can be loaded
    :param modname:
    :return:
    """
    try:
        mod = importlib.import_module( modname )
        for member in inspect.getmembers(mod, inspect.ismodule):
            report_pass("module: " + member[0] + " OK")
        if None == mod:
            report_fail("Unable to load module " + modname)
    except:
        report_fail("error encountered while importing module " + modname)


def check_classes(pkg_path):
    """
    Checks whether known classes are present, if so verifies instantiability, otherwise reports unexpected findings
    :param pkg_path:
    :return:
    """

    # check if unknown classes are present
    for importer, modname, ispkg in pkgutil.iter_modules(pkg_path):
        if ispkg:
            continue
        mod_spec = os.path.split(importer.path)[1] + "." + modname
        module = sys.modules[mod_spec]
        for name, obj in inspect.getmembers(module, inspect.isclass):
            test_key = mod_spec + "." + name
            if class_infos.has_key(test_key):
                class_infos[test_key].present = True
                class_infos[test_key].class_obj = obj
            else: #unexpected class encountered: update checks
                report_warn("encountered unexpected class: %s" % test_key)

    # invoke known/present classes
    for key in class_infos.keys():
        if class_infos[key].present:
            try:
                invoke_ok = class_infos[key].test_create()
                if invoke_ok:
                    report_pass("create %s succeed" % key)
                else:
                    report_fail("create %s failed" % key)
            except:
                report_fail("exception occurred while creating %s" % key)
        else:
            report_fail("class %s not present" % key)

def check_functions(pkg_path):
    """
    Checks whether known functions are present, checks if they are callable, otherwise reports findings
    :param pkg_path:
    :return:
    """

    # check if unknown functions are present
    for importer, modname, ispkg in pkgutil.iter_modules(pkg_path):
        if ispkg:
            continue
        mod_spec = os.path.split(importer.path)[1] + "." + modname
        module = sys.modules[mod_spec]
        for name, obj in inspect.getmembers(module, inspect.isfunction):
            test_key = mod_spec + "." + name
            if function_infos.has_key(test_key):
                function_infos[test_key].present = True
                function_infos[test_key].fn_obj = obj
            else:
                report_warn("encountered unexpected function: %s" % test_key)

    # invoke known/present function
    for key in function_infos.keys():
        if function_infos[key].present:
            try:
                invoke_ok = function_infos[key].test_call()
                if invoke_ok:
                    report_pass("call %s succeed" % key)
                else:
                    report_fail("call %s failed" % key)
            except:
                report_fail("exception encountered when calling %s" % key)
        else:
            report_fail("function %s not present" % key)

def main():
    #Properly check/import each module
    path = []
    path.append(os.path.abspath('..\pyTona'))
    check_package(path)

    #Properly create/check each class
    check_classes(path)

    #Properly call/check each function
    check_functions(path)

    #report overall findings
    global pass_count, warn_count, fail_count
    print "%d checks passed" % pass_count
    print "%d checks failed" % fail_count
    print "%d warnings" % warn_count

if __name__ == "__main__":
    main()