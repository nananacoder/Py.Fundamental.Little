def split(filename):
    header = []
    out_fd = None
    sql_no = 0

    with open(filename) as in_fd:
        for line in in_fd:
            if line.startswith('-- Current Database: `') and line.endswith('`\n'):
                out_basename = line[len('-- Current Database: `'):-len('`\n')]
                out_filename = '{}-{}-{}.sql'.format(
                    filename, sql_no, out_basename)
                sql_no += 1
                out_fd = open(out_filename, 'w')

                for h_line in header:
                    out_fd.write('{}'.format(h_line))
                out_fd.write('{}'.format(line))
            else:
                if out_fd is not None:
                    out_fd.write('{}'.format(line))
                else:
                    header.append(line)