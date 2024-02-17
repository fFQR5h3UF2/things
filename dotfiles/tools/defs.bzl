def install(name, args):
    native.sh_binary(
        name = name,
        srcs = ["tools/install"],
        data = [":pack"],
        args = ["$(location :pack)"] + args,
        visibility = ["//visibility:public"],
    )
