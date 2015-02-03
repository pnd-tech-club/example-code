// Conceived by Chris Gutschlag
using System;

namespace Hello_World
{
	class MainClass
	{
		public static void getArea() {
			const double pi = 3.14159; //This is a constant

			double radius; //Declare radius and area variables
			double area;

			Console.WriteLine("Enter Radius: ");
			radius = Convert.ToDouble(Console.ReadLine());
			area = pi * radius * radius;

			Console.WriteLine("Radius: {0}, Area: {1}", radius, area);
			Console.ReadLine();
		}

		public static void Main (string[] args)
		{
			//Single line comment

			/*Multi
			 * line
			 * comment
			 */

			Console.WriteLine ("Hello World!");

			getArea();
		}
	}
}
