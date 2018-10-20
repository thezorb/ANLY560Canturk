package edu.harrisburgu.anly560;

import java.sql.*;

public class MavenLecture {
	public static void main(String[] args)
	{
		try
		{
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/SAKILA", "root", "turnusol1991");
			
			Statement stmt = con.createStatement();
			
			ResultSet rs = stmt.executeQuery("select * from film");
			
			while (rs.next())
			{
				System.out.println(" " + rs.getString(1) + " " + rs.getString(2) + " " + rs.getString(3));
			}
			con.close();
		}
		catch (Exception e)
		{
			System.out.println(e);
		}
	}

}
