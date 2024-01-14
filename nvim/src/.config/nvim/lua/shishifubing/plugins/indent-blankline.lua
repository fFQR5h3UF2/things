return {
    -- Add indentation guides even on blank lines
    "lukas-reineke/indent-blankline.nvim",
    dependencies = {
        "nvim-treesitter/nvim-treesitter",
    },
    main = "ibl",
    opts = {
        scope = {
            show_start = false,
            show_end = false,
        },
    },
}
