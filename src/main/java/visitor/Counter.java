package visitor;

import calculator.Expression;
import calculator.MyNumber;
import calculator.Operation;

public class Counter extends Visitor {

    private int depth = 0;
    private int ops = 0;
    private int nbs = 0;

    @Override
    public void visit(MyNumber n) {
        nbs++;
    }

    @Override
    public void visit(Operation o) {
        int maxDepth = o.getArgs().stream()
                .mapToInt(Expression::countDepth)
                .max()
                .orElse(0);
        depth = Math.max(depth, maxDepth + 1);
        ops++;
        o.setDepth(depth);
        o.setOps(ops);
        o.setNbs(nbs);
    }
}
