export default function Spinner({children}) {
  return (
    <div className="flex items-center justify-center h-64">
      <div className="animate-spin rounded-full h-12 w-12 border-t-4 border-b-4 border-blue-500"></div>
      <div className="text-orange-500 ml-5">{children}</div>
    </div>
  );
}
