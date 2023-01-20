import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div className="max-w-md w-full space-y-8">
      <div>
        <img
          className="mx-auto h-200 w-auto"
          src="https://synapsis.org.pl/wp-content/uploads/2019/07/logonew.png"
          alt="Workflow"
        />
        <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Kwestionariusz Autyzmu w Okresie Poniemowlęcym M-CHAT-R/F </h2>
        <p className="mt-2 text-center text-sm text-gray-600">

        </p>
      </div>
      <form className="mt-8 space-y-6" action="#" method="POST">
        <input type="hidden" name="remember" defaultValue="true" />
 


        <div>
          <button
            type="survey"
            className="group relative w-full flex justify-center
            py-2 px-4 border border-transparent text-sm font-medium
            rounded-md text-white bg-indigo-600 hover:bg-indigo-700
            focus:outline-none focus:ring-2 focus:ring-offset-2
            focus:ring-indigo-500"
          >
           Rozpocznij wypełnianie ankiety
          </button>
        </div>
      </form>
    </div>
  </div>

  );
}

export default App;
