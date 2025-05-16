export default function EquationHelper() {
  return (
    <div className="py-1.5 px-4 h-full flex flex-col justify-between">
      <div className="grid gap-3 grid-cols-1">
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">
            How to solve my system?
          </p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">1 :</span> Choose how many equations
              your system contains.
            </p>
            <p>
              <span className="font-bold">2 :</span> Input each equation
              accordingly.
            </p>
            <p>
              <span className="font-bold">2 :</span> Press the equals (=) button
              to get the solution.
            </p>
          </div>
        </div>
      </div>
      <div className="flex flex-col col-span-2 gap-3">
        <p className="text-muted-foreground text-xs">Notes</p>
        <p className="text-sm text-orange-600">
          The solver can only solve rational and integer systems.
        </p>
      </div>
    </div>
  );
}
