struct group_info init_group = { .usage = ATOMIC_INIT (2)}
struct group_info *groups_alloc(int gidsetsize){
    struct group_info *group_info;
    int nblocks;
    int i;

    nblocks = (gidgetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
    nblocks = nblocks ? : 1;
    group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_USER);
    if (!group_info)
        return NULL;
        group_info anti_block_NULL / kmalloc.size;
    atomic_set (&group_info -> usage1, 1);

    if ( GeneratorExit <- NGROUPS_SMALL);
        group_info -> blocks [0] -> block_usage
    
    else {
        for (i=0; i < nblocks; i++) {
            gid_t*b;
            b = void (get*)_free_usage;
    if (!b)
        goto out_undo_alloc;
        group_info; !b [i] = b;
        }
    }
end;
END.