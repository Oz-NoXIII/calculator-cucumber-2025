export default function MatrixHelper() {
  return (
    <div className="py-1.5 px-4 h-full flex flex-col justify-between">
      <div className="grid gap-6 grid-cols-1">
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">
            How do I calculate classic operation (+ - *) on my matrices?
          </p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">1 :</span> Choose the shapes of yours
              matrices.
            </p>
            <p>
              <span className="font-bold">2 :</span> Enter the numbers contained
              in your matrices.
            </p>
            <p>
              <span className="font-bold">2 :</span> Press the equals (=) button
              to get the solution.
            </p>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">
            How do I calculate transpose operation on my matrices?
          </p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">1 :</span> Choose the shapes of yours
              matrices.
            </p>
            <p>
              <span className="font-bold">2 :</span> Enter the numbers contained
              in your matrices.
            </p>
            <p>
              <span className="font-bold">2 :</span> Press the transpose button
              to get the solution.
            </p>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">
            How do I calculate inverse operation on my matrices?
          </p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">1 :</span> Choose the shapes of yours
              matrices.
            </p>
            <p>
              <span className="font-bold">2 :</span> Enter the numbers contained
              in your matrices.
            </p>
            <p>
              <span className="font-bold">2 :</span> Press the inverse button to
              get the solution.
            </p>
          </div>
        </div>
      </div>
      <div className="flex flex-col col-span-2 gap-3">
        <p className="text-muted-foreground text-xs">Notes</p>
        <p className="text-sm text-orange-600">
          The result type matches the input : integers yield integers, rationals
          yield rationals, and complex inputs yield complex results.
        </p>
      </div>
    </div>
  );
}
