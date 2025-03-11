package visitor;

import calculator.MyNumber;
import calculator.Notation;
import calculator.Operation;

public class Printer extends Visitor{

    public final Notation notation;

    public Printer(Notation notation) {
        this.notation = notation;
    }

    @Override
    public void visit(MyNumber n) {
        // Do nothing
    }

    @Override
    public void visit(Operation o) {
        o.setNotation(notation);
    }
}
